# Evaluation framework

LLM output quality must be measurable. This repo uses a lightweight approach that is easy to run in CI.

## What we test

- **Structure**: required sections exist
- **Safety**: forbidden patterns are absent (e.g., “I think it does X”)
- **Traceability**: outputs reference inputs and avoid invention
- **Clarity**: consistent headings, concise language

## What we *don’t* claim

This is not a full semantic evaluation. It is a pragmatic baseline.

## Next upgrades

- Golden datasets tied to real doc tasks
- Model/provider comparison
- LLM-as-judge with strict rubrics

