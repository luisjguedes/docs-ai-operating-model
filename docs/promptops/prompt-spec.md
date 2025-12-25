# Prompt spec

Prompt files live in `prompts/` as YAML.

## Required fields

- `id`: stable identifier  
- `version`: semantic version for changes  
- `task`: the thing this prompt does  
- `prompt`: the actual prompt content  
- `constraints`: list of non-negotiables  

## Example

```yaml
id: release_notes_draft
version: 1.0.0
task: release_notes
prompt: |
  You are a senior technical writer...
constraints:
  - Do not invent features.
  - Use headings: Summary, Changes, Fixes.
```

