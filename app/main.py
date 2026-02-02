# Simple health check tool
import logging
import time
from fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, Response
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

@mcp.custom_route("/flights", methods=["GET"])
async def get_flights(request):
    # Implement your logic to fetch and return flight data here
    return JSONResponse(
        content={"flights": [   
            { "id": 1, "price": 230, "duration minutes": 65, "company": "finnair", "stops": 0, "depart_iso": "2025-10-15T15:00:00Z", "arrive_iso": "2025-10-15T16:05:00Z" }, 
            { "id": 2, "price": 30, "duration minutes": 65, "company": "air china", "stops": 0, "depart_iso": "2025-10-15T08:00:00Z", "arrive_iso": "2025-10-15T09:05:00Z" }, 
            { "id": 3, "price": 120, "duration minutes": 75, "company": "norwegian", "stops": 0, "depart_iso": "2025-10-15T12:00:00Z", "arrive_iso": "2025-10-15T13:15:00Z" } 
        ]},
        status_code=200)

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