---
name: skill-creator
description: Creates new ADK-compatible skill definitions from requirements and produces complete SKILL.md files that follow the Agent Skills specification.
---

# Skill Creator

Use this skill when the user asks to create a new Agent Skill.

## Required workflow

1. Determine the purpose of the new skill.
2. Choose a clear kebab-case name, for example `code-review` or `release-checklist`.
3. Write a compact description that explains when the skill should be used.
4. Create a directory whose name matches the skill name.
5. Add a `SKILL.md` file with YAML frontmatter and markdown instructions.
6. Add `references/` materials only when the instructions are long or need supporting context.
7. Keep the skill focused, practical, and reusable.

## SKILL.md format

Every skill directory must contain a `SKILL.md` file.

```yaml
---
name: my-skill-name
description: What this skill does.
---
```

The body of the file contains markdown instructions that tell the agent how to behave.

## Directory structure

```text
my-skill-name/
  SKILL.md
  references/
  assets/
  scripts/
```

## Rules

- The directory name must match the `name` field in frontmatter.
- Use lowercase kebab-case.
- Keep the description under 1024 characters.
- Instructions should be clear and step-by-step.
- Use `references/` for detailed supporting documents.
- Keep `SKILL.md` concise; move longer details into references.
- Output the full file content so it can be saved directly.

## Example

```markdown
---
name: code-review
description: Reviews Python code for correctness, style, and performance.
---

# Code Review Instructions

When asked to review code:

## Step 1: Read the guidelines
Use the checklist in `references/review-checklist.md`.

## Step 2: Analyze
Check the code for correctness, readability, and performance issues.

## Step 3: Report
Summarize findings by severity.
```

## Required references

- `references/skill-spec.md`
- `references/example-skill.md`
