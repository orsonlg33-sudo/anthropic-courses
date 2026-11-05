import sys
import asyncio
from typing import Optional, Any
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import json
from pydantic import AnyUrl


class MCPClient:
    def __init__(
        self,
        command: str,
        args: list[str],
        env: Optional[dict] = None,
    ):
        self._command = command
        self._args = args
        self._env = env
        self._session: Optional[ClientSession] = None
        self._exit_stack: AsyncExitStack = AsyncExitStack()

    async def connect(self):
        server_params = StdioServerParameters(
            command=self._command,
            args=self._args,
            env=self._env,
        )
        stdio_transport = await self._exit_stack.enter_async_context(
            stdio_client(server_params)
        )
        _stdio, _write = stdio_transport
        self._session = await self._exit_stack.enter_async_context(
            ClientSession(_stdio, _write)
        )
        await self._session.initialize()

    def session(self) -> ClientSession:
        if self._session is None:
            raise ConnectionError(
                "Client session not initialized or cache not populated. Call connect_to_server first."
            )
        return self._session

    async def list_tools(self) -> list[types.Tool]:
        # self.session() is the live connection to the MCP server
        result = await self.session().list_tools()
        # The result object wraps the tools, so we return only the list
        return result.tools

    async def call_tool(
        self, tool_name: str, tool_input: dict
    ) -> types.CallToolResult | None:
        # Send the tool name and Claude's input arguments to the server
        # The server runs the tool and returns the result
        return await self.session().call_tool(tool_name, tool_input)

    async def list_prompts(self) -> list[types.Prompt]:
        # Ask the server for every prompt it defines
        result = await self.session().list_prompts()
        # The result wraps the prompts, so we return only the list
        return result.prompts

    async def get_prompt(self, prompt_name, args: dict[str, str]):
        # args holds the prompt's parameters, such as {"doc_id": "plan.md"}
        # The server inserts them into the prompt template
        result = await self.session().get_prompt(prompt_name, args)
        # The messages can be sent straight to Claude
        return result.messages

    async def read_resource(self, uri: str) -> Any:
        # Ask the server for the resource, wrapping the string in AnyUrl
        result = await self.session().read_resource(AnyUrl(uri))
        # The response holds a list of contents, and we only need the first
        resource = result.contents[0]

        # Text resources carry their data in .text
        if isinstance(resource, types.TextResourceContents):
            # The MIME type tells us how to parse it
            if resource.mimeType == "application/json":
                # JSON becomes a Python object, such as a list of doc ids
                return json.loads(resource.text)

            # Anything else (such as text/plain) stays as a string
            return resource.text

    async def cleanup(self):
        await self._exit_stack.aclose()
        self._session = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup()


# For testing
async def main():
    async with MCPClient(
        # We use plain python instead of uv, so "run" is removed from args
        command="python",
        args=["mcp_server.py"],
    ) as client:
        # Direct resource: should print a Python list of document ids
        doc_ids = await client.read_resource("docs://documents")
        print(doc_ids)

        # Templated resource: should print the text of one document
        plan = await client.read_resource("docs://documents/plan.md")
        print(plan)


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())
