from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]


REQUIRED_PROMPT_KEYS = {
    "id",
    "version",
    "task",
    "prompt",
    "constraints",
}


@dataclass
class EvalResult:
    case_id: str
    passed: bool
    errors: list[str]


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_prompt_file(path: Path) -> list[str]:
    data = load_yaml(path)
    errors: list[str] = []

    if not isinstance(data, dict):
        return [f"{path}: prompt file must be a YAML mapping"]

    missing = REQUIRED_PROMPT_KEYS - set(data.keys())
    if missing:
        errors.append(f"{path}: missing keys: {sorted(missing)}")

    # Lightweight shape checks
    if "constraints" in data and not isinstance(data["constraints"], list):
        errors.append(f"{path}: constraints must be a list")

    if "prompt" in data and not isinstance(data["prompt"], str):
        errors.append(f"{path}: prompt must be a string")

    return errors


def cmd_validate_prompts(_: argparse.Namespace) -> int:
    prompts_dir = REPO_ROOT / "prompts"
    prompt_files = sorted(prompts_dir.glob("*.yml")) + sorted(prompts_dir.glob("*.yaml"))

    if not prompt_files:
        print("No prompt files found in prompts/ (expected *.yml or *.yaml).")
        return 1

    all_errors: list[str] = []
    for p in prompt_files:
        all_errors.extend(validate_prompt_file(p))

    if all_errors:
        print("Prompt validation failed:")
        for e in all_errors:
            print(f"- {e}")
        return 1

    print(f"OK: {len(prompt_files)} prompt file(s) validated.")
    return 0


def cmd_eval(args: argparse.Namespace) -> int:
    dataset = Path(args.dataset)
    if not dataset.exists():
        print(f"Dataset not found: {dataset}")
        return 1

    data = load_yaml(dataset)
    cases = data.get("cases", [])
    if not isinstance(cases, list) or not cases:
        print("Dataset must define a non-empty list: cases:")
        return 1

    # This is intentionally a DRY-RUN harness: it checks the evaluation spec,
    # and demonstrates how you'd gate outputs in CI, without requiring API keys.
    results: list[EvalResult] = []
    for case in cases:
        case_id = case.get("id", "<missing-id>")
        expected = case.get("expected", {})
        errors: list[str] = []

        required = expected.get("required_headings", [])
        forbidden = expected.get("forbidden_phrases", [])
        if required and not isinstance(required, list):
            errors.append("expected.required_headings must be a list")
        if forbidden and not isinstance(forbidden, list):
            errors.append("expected.forbidden_phrases must be a list")

        # In a real pipeline, you'd generate output here and check it.
        if args.dry_run:
            pass

        results.append(EvalResult(case_id=case_id, passed=(len(errors) == 0), errors=errors))

    failed = [r for r in results if not r.passed]
    if failed:
        print("Evaluation spec validation failed:")
        for r in failed:
            for e in r.errors:
                print(f"- {r.case_id}: {e}")
        return 1

    print(f"OK: {len(results)} case(s) validated (dry-run={args.dry_run}).")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="docsai", description="Docs AI Operating Model utilities")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_val = sub.add_parser("validate-prompts", help="Validate prompt YAML files in prompts/")
    p_val.set_defaults(func=cmd_validate_prompts)

    p_eval = sub.add_parser("eval", help="Validate evaluation dataset (dry-run harness)")
    p_eval.add_argument("--dataset", required=True, help="Path to dataset YAML (e.g., eval/datasets/smoke.yml)")
    p_eval.add_argument("--dry-run", action="store_true", help="Do not call any LLM provider")
    p_eval.set_defaults(func=cmd_eval)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
