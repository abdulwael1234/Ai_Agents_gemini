#!/usr/bin/env python3
"""Call a tool on the practice MCP server without any agent, to test it.

  call_tool.py                         list the server's tools
  call_tool.py TOOL [key=value ...]    call one tool and print the result

Run from the repository root. Uses tools/mcp/guards_server.py.
"""
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER = StdioServerParameters(command=sys.executable, args=["tools/mcp/guards_server.py"])


async def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    async with stdio_client(SERVER) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            if len(sys.argv) == 1:
                for tool in (await session.list_tools()).tools:
                    print(f"{tool.name}: {(tool.description or '').strip().splitlines()[0]}")
                return 0
            arguments = dict(pair.split("=", 1) for pair in sys.argv[2:])
            result = await session.call_tool(sys.argv[1], arguments)
            for item in result.content:
                print(getattr(item, "text", item))
            return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
