---
name: verify-repo
description: Verifies the repository before committing or pushing. Use after finishing a change, before a commit or push, or when the user asks to check, verify or validate the repo. Checks for leaked API keys, tracked .env files and BOM characters.
allowed-tools: Bash(powershell -File *), Bash(git status *)
---

When verifying the repository:

1. Run `powershell -File .claude/skills/verify-repo/check.ps1` from the repo root. Run the script, do not read it.
2. Report each check as pass or fail, quoting the script output as evidence.
3. If any check fails, do not commit or push. List the offending files and what to change.
4. Run `git status --short` and confirm that no unexpected files are staged.