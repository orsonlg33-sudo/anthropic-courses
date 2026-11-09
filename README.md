# Anthropic Courses

My hands-on work from Claude Academy courses, kept in one repository with one folder per course.

## Courses

### Building with the Claude API (completed November 2026)

Credential: https://academy.claude.com/verify/86641044313fd35d72419f5c5d60c6d9

Folder: `building-with-the-claude-api/`

What is inside:

- **Notebooks** (`lesson_*.ipynb`): one runnable notebook per lesson, covering requests and system prompts, temperature, streaming, evals (model and code graders), prompt engineering, tool use, the text editor and web search tools, RAG (chunking, embeddings, BM25 and hybrid retrieval), extended thinking, vision, citations, prompt caching, and code execution with the Files API.
- **MCP project** (`cli_project/`): a document chatbot for the command line. It includes an MCP server with tools, resources and prompts, and an MCP client that connects them to Claude.

### Introduction to Agent Skills (completed November 2026)

Folder: `introduction-to-agent-skills/`

What is inside:

- **pr-description skill** (`introduction-to-agent-skills/skills/pr-description/`): a Claude Code skill that writes pull request descriptions in a fixed What / Why / Changes format. It uses `allowed-tools` to pre-approve read-only git commands, and a `references/` file that is loaded only when an example is needed (progressive disclosure).
- **Shared project skill** (`.claude/skills/pr-description/`): the same skill committed to the repo, so anyone who clones it receives the skill automatically. It passes `claude plugin validate`.

This course needs no Python environment.

## Setup (Python courses)

1. Create and activate an environment, then install the packages: `python -m venv .venv`, then `.\.venv\Scripts\Activate.ps1`, then `python -m pip install -r requirements.txt`.
2. Create a `.env` file in the course folder with your own keys: `ANTHROPIC_API_KEY=your_key_here` and `VOYAGE_API_KEY=your_key_here`.
3. Open the notebooks with `python -m notebook`.

For the MCP project, go into `cli_project/`, create its own environment from its `requirements.txt`, add a `.env` with `ANTHROPIC_API_KEY` and `USE_UV=0`, and run `python main.py`.

## Notes

Keys are never committed. The `.env` files are listed in `.gitignore`.