from fastmcp import FastMCP
from tools import system, routing, switching


mcp = FastMCP("home-network")
mcp.mount(system.mcp)
mcp.mount(routing.mcp)
mcp.mount(switching.mcp)


if __name__ == "__main__":
    mcp.run()
