# Example: Code Review Skill

```markdown
---
name: code-review
description: Reviews Python code for correctness, style, and performance. Checks for common bugs, PEP 8 compliance, and suggests optimizations.
---

# Code Review Instructions

When asked to review code:

## Step 1: Read the guidelines
Use `load_skill_resource` to read `references/review-checklist.md`.

## Step 2: Analyze
Check the code against each item in the checklist.

## Step 3: Report
Provide findings organized by severity:
- Critical: bugs, security risks
- Warning: style issues, performance concerns
- Info: suggestions for improvement
```

This example shows the expected structure for a valid Agent Skill directory.
