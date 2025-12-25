# Docs AI Operating Model (template)

A **docs-as-code + LLM strategy** reference implementation you can fork to bootstrap:
- a documentation site (MkDocs)
- a PromptOps library (prompts as code, with review + validation)
- an evaluation harness (quality gates for AI-assisted writing)
- a governance pack (policies, risk register, ADRs, metrics)

> **Portfolio note**
>
> All content in this repository is **generic and non-proprietary**. It is meant to demonstrate senior-level thinking and execution for documentation leaders and AI-forward technical writers.

---

## Why this repo exists

Docs teams are being asked to “use AI” — but the real work is:
- **deciding** which problems are worth solving with LLMs
- **controlling risk** (privacy, hallucinations, IP, compliance)
- **operationalizing quality** (repeatable evaluation, measurable outcomes)
- **integrating into DocsOps** (CI/CD, style gates, review workflows)

This repo is designed to **show your seniority** by making those decisions visible.

---

## What it demonstrates

### Docs-as-code (DocsOps)
- Site authored in Markdown and published with MkDocs
- CI quality gates: build checks + prose linting
- A consistent information architecture (strategy → governance → implementation → case studies)

### LLM strategy (operating model)
- Use-case catalog + decision criteria
- Guardrails: data classification, risk register, human review lanes
- Metrics: adoption, quality, efficiency, and customer impact

### PromptOps (prompts as code)
- Prompt files stored with metadata and versioning
- Schema validation in CI (no broken prompt definitions)
- Patterns for prompt structure and output contracts

### Evaluation (what “good” means)
- Task-based evaluation dataset (small but realistic)
- Rule-based checks for structure + safety
- Optional “LLM-as-judge” extension points (vendor-agnostic)

---

## Quick start (local)

```bash
# 1) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 2) Install deps
pip install -r requirements.txt
pip install -r requirements-docs.txt

# 3) Validate the prompt library
python -m docsai_toolkit validate-prompts

# 4) Build the site (strict)
mkdocs build --strict

# 5) Run a lightweight evaluation pass
python -m docsai_toolkit eval --dataset eval/datasets/smoke.yml --dry-run
```

---

## Publish the docs site (GitHub Pages)

This repo includes a Pages workflow that:
1) builds the MkDocs site
2) uploads it as a Pages artifact
3) deploys it via `actions/deploy-pages`

In your repo settings:
- **Settings → Pages → Source → GitHub Actions**

---

## Repository map

```
docs/                 # the published site (strategy, governance, implementation)
prompts/              # prompt library (YAML)
eval/                 # evaluation datasets + rubrics
adr/                  # architecture decision records
src/docsai_toolkit/   # small CLI utilities (validation + eval scaffolding)
.github/workflows/    # CI + Pages deployment
styles/               # Vale prose linting rules (optional but recommended)
```

---

## Suggested ways to personalize (for hiring impact)

- Add a **case study** reflecting your strongest domain (SaaS, MDM, APIs, data governance)
- Add a **short demo video** (60–90s) showing: PR → CI → Pages → prompt validation → eval report
- Add a “**Hiring?**” section with your role targets and preferred work style (remote-first, async)

---

## License

MIT (see `LICENSE`).
