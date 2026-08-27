# Agent Skills Specification

## SKILL.md Format

Every skill directory must contain a `SKILL.md` file.

### Frontmatter

```yaml
---
name: my-skill-name
description: What this skill does.
---
```

### Supported metadata

- `name`: required, lowercase kebab-case or snake_case
- `description`: required, concise and action-oriented
- `license`: optional
- `compatibility`: optional
- `allowed-tools`: optional experimental field
- `metadata`: optional key-value data

### Body content

The body of `SKILL.md` is markdown instruction content. It should tell the agent:

- when to use the skill
- what process or workflow to follow
- what checks to apply
- how to structure outputs

### Directory layout

```text
my-skill-name/
  SKILL.md
  references/
  assets/
  scripts/
```

## Discovery model

Skills are loaded progressively:

1. Discovery loads only `name` and `description`.
2. Activation reads the full `SKILL.md`.
3. Execution may load references or scripts.

## Important constraints

- Keep the directory name and skill name aligned.
- Keep the description under 1024 characters.
- Keep the instructions clear and actionable.
- Store long details in `references/` instead of the main file.
