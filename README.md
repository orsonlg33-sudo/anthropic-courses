\# Anthropic Courses



My hands-on work from Claude Academy courses, kept in one repository with one folder per course.



\## Courses



\### Building with the Claude API (completed November 2026)



Credential: https://academy.claude.com/verify/86641044313fd35d72419f5c5d60c6d9



Folder: `building-with-the-claude-api/`



What is inside:



\- \*\*Notebooks\*\* (`lesson\_\*.ipynb`): one runnable notebook per lesson, covering requests and system prompts, temperature, streaming, evals (model and code graders), prompt engineering, tool use, the text editor and web search tools, RAG (chunking, embeddings, BM25 and hybrid retrieval), extended thinking, vision, citations, prompt caching, and code execution with the Files API.

\- \*\*MCP project\*\* (`cli\_project/`): a document chatbot for the command line. It includes an MCP server with tools, resources and prompts, and an MCP client that connects them to Claude.



\## Setup



1\. Create and activate an environment, then install the packages:

&#x20;  ```

&#x20;  python -m venv .venv

&#x20;  .\\.venv\\Scripts\\Activate.ps1

&#x20;  python -m pip install -r requirements.txt

&#x20;  ```

2\. Create a `.env` file in the course folder with your own keys:

&#x20;  ```

&#x20;  ANTHROPIC\_API\_KEY=your\_key\_here

&#x20;  VOYAGE\_API\_KEY=your\_key\_here

&#x20;  ```

3\. Open the notebooks with `python -m notebook`.



For the MCP project, go into `cli\_project/`, create its own environment from its `requirements.txt`, add a `.env` with `ANTHROPIC\_API\_KEY` and `USE\_UV=0`, and run `python main.py`.



\## Notes



Keys are never committed. The `.env` files are listed in `.gitignore`.

