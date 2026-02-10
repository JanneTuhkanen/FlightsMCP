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

@mcp.tool("/flights")
async def get_flights() -> JSONResponse:
    """
    Docstring for get_flights tool. This tool returns a list of available flights with details such as price, duration, company, stops, and departure/arrival times in ISO format.
    
    :return: JSONResponse
    """
    return JSONResponse(
        content={"flights": [   
            { "id": 1, "price": 230, "duration minutes": 65, "company": "finnair", "stops": 0, "destination": "Paris", "depart_iso": "2026-10-15T15:00:00Z", "arrive_iso": "2026-10-15T16:05:00Z" }, 
            { "id": 2, "price": 30, "duration minutes": 65, "company": "air china", "stops": 0, "destination": "Beijing", "depart_iso": "2026-10-15T08:00:00Z", "arrive_iso": "2026-10-15T09:05:00Z" }, 
            { "id": 3, "price": 120, "duration minutes": 75, "company": "norwegian", "stops": 0, "destination": "Oslo", "depart_iso": "2026-10-15T12:00:00Z", "arrive_iso": "2026-10-15T13:15:00Z" },
            { "id": 4, "price": 185, "duration minutes": 90, "company": "lufthansa", "stops": 1, "destination": "Berlin", "depart_iso": "2026-10-15T10:30:00Z", "arrive_iso": "2026-10-15T12:00:00Z" },
            { "id": 5, "price": 95, "duration minutes": 120, "company": "ryanair", "stops": 2, "destination": "London", "depart_iso": "2026-10-16T06:00:00Z", "arrive_iso": "2026-10-15T08:00:00Z" },
            { "id": 6, "price": 280, "duration minutes": 55, "company": "swiss", "stops": 0, "destination": "Paris", "depart_iso": "2026-10-16T18:00:00Z", "arrive_iso": "2026-10-15T18:55:00Z" },
            { "id": 7, "price": 150, "duration minutes": 85, "company": "klm", "stops": 1, "destination": "Beijing", "depart_iso": "2026-10-16T14:00:00Z", "arrive_iso": "2026-10-15T15:25:00Z" },
            { "id": 8, "price": 110, "duration minutes": 100, "company": "wizz air", "stops": 1, "destination": "Berlin", "depart_iso": "2026-10-17T07:30:00Z", "arrive_iso": "2026-10-15T09:10:00Z" },
            { "id": 9, "price": 210, "duration minutes": 70, "company": "british airways", "stops": 0, "destination": "London", "depart_iso": "2026-10-18T16:45:00Z", "arrive_iso": "2026-10-15T17:55:00Z" },
            { "id": 10, "price": 175, "duration minutes": 95, "company": "easyjet", "stops": 1, "destination": "Oslo", "depart_iso": "2026-10-18T11:00:00Z", "arrive_iso": "2026-10-15T12:35:00Z" },
            { "id": 11, "price": 240, "duration minutes": 60, "company": "iberia", "stops": 0, "destination": "Paris", "depart_iso": "2026-10-18T13:00:00Z", "arrive_iso": "2026-10-15T14:00:00Z" },
            { "id": 12, "price": 85, "duration minutes": 140, "company": "flixbus air", "stops": 2, "destination": "Beijing", "depart_iso": "2026-10-18T05:00:00Z", "arrive_iso": "2026-10-15T07:20:00Z" },
            { "id": 13, "price": 195, "duration minutes": 80, "company": "alitalia", "stops": 1, "destination": "London", "depart_iso": "2026-10-19T09:00:00Z", "arrive_iso": "2026-10-15T10:20:00Z" },
            { "id": 14, "price": 260, "duration minutes": 65, "company": "sas", "stops": 0, "destination": "Berlin", "depart_iso": "2026-10-19T17:30:00Z", "arrive_iso": "2026-10-15T18:35:00Z" },
            { "id": 15, "price": 130, "duration minutes": 110, "company": "norwegian", "stops": 2, "destination": "Oslo", "depart_iso": "2026-10-20T06:30:00Z", "arrive_iso": "2026-10-15T08:20:00Z" },
            { "id": 16, "price": 220, "duration minutes": 75, "company": "air france", "stops": 0, "destination": "Paris", "depart_iso": "2026-10-20T15:30:00Z", "arrive_iso": "2026-10-15T16:45:00Z" },
            { "id": 17, "price": 140, "duration minutes": 105, "company": "vueling", "stops": 1, "destination": "Beijing", "depart_iso": "2026-10-21T12:00:00Z", "arrive_iso": "2026-10-15T13:45:00Z" },
            { "id": 18, "price": 200, "duration minutes": 70, "company": "tap air portugal", "stops": 0, "destination": "London", "depart_iso": "2026-10-21T14:15:00Z", "arrive_iso": "2026-10-15T15:25:00Z" },
            { "id": 19, "price": 165, "duration minutes": 90, "company": "finnair", "stops": 1, "destination": "Berlin", "depart_iso": "2026-10-21T10:00:00Z", "arrive_iso": "2026-10-15T11:30:00Z" },
            { "id": 20, "price": 105, "duration minutes": 125, "company": "spirit airlines", "stops": 2, "destination": "Oslo", "depart_iso": "2026-10-21T04:30:00Z", "arrive_iso": "2026-10-15T06:35:00Z" }
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