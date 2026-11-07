---
name: pr-description
description: Writes pull request descriptions. Use when creating a PR, writing a PR, or when the user asks to summarize changes for a pull request.
allowed-tools: Bash(git diff *), Bash(git log *)
---

When writing a PR description:

1. Run `git diff main...HEAD` to see all changes on this branch
2. Write a description following this format:

## What
One sentence explaining what this PR does.

## Why
Brief context on why this change is needed

## Changes
- Bullet points of specific changes made
- Group related changes together
- Mention any files deleted or renamed

## Examples
If the user asks for an example, or the change is large and the format is unclear, read [references/format-examples.md](references/format-examples.md). Otherwise do not load it.