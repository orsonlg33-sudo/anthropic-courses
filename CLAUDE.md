# Project rules

- IMPORTANT: Keep API keys only in local `.env` files, never in code, notebooks or commits. Read them with `python-dotenv` or `os.getenv`.
- Give each course folder its own `.venv` and `requirements.txt`. Install packages only into that course's environment.
- Save files as UTF-8 without a BOM. In Windows PowerShell 5.1, write files with `[System.IO.File]::WriteAllText` and `UTF8Encoding($false)`, not `Set-Content -Encoding utf8`.
- Put new course material in a new top-level folder named after the course in lowercase with hyphens, for example `claude-code-in-action/`.