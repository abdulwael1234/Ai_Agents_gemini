#!/usr/bin/env python3
"""A tiny MCP server with one tool: the header-guard check from lesson 6."""
import subprocess
import sys
from pathlib import Path

try:                                                 # mcp 2.x
    from mcp.server.mcpserver import MCPServer
except ImportError:                                  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as MCPServer

ROOT = Path(__file__).resolve().parents[2]          # repository root
SCRIPT = ROOT / ".agents" / "skills" / "header-guards" / "scripts" / "check_guards.py"

mcp = MCPServer("fwpractice")


@mcp.tool()
def check_header_guards(folder: str = "src") -> str:
    """Check that every C header under a folder of this repository has an include
    guard named after its file. Returns one line per problem and a summary line."""
    target = (ROOT / folder).resolve()
    if target != ROOT and ROOT not in target.parents:
        return "error: the folder must be inside the repository"
    result = subprocess.run([sys.executable, str(SCRIPT), str(target)],
                            capture_output=True, text=True, timeout=60)
    return (result.stdout + result.stderr).strip() or "no output"


if __name__ == "__main__":
    mcp.run()                                        # stdio transport
