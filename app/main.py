# Simple health check tool
import logging
import time
from fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware
import mcp

from settings import APP_VERSION

SERVICE = "template-mcp-server"
START = time.time()
_logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="Tempate MCP Server Project",
    instructions="Jump-start your MCP server development with this template project.",
)

@mcp.tool()
async def health() -> dict:
    _logger.info("Health called")

    """Health check tool for the MCP server. Use this to verify that the service is running."""
    return {
        "status": "ok",
        "service": SERVICE,
        "version": APP_VERSION,
        "uptime_seconds": int(time.time() - START),
    }

app = mcp.http_app()

# Add custom (Starlette) CORS middleware to the FastMCP server for web client support
app.add_middleware(
    CORSMiddleware,
    # change allow_origins according to your needs during development
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_logger.info(f"{SERVICE} VERSION {APP_VERSION} started")