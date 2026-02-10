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
async def get_flights() -> dict:
    """
    Docstring for get_flights tool. This tool returns a list of available flights with details such as price, company, stops, and departure/arrival times in ISO format.
    Duration should be calculated from the departure and arrival times upon receiving the request, and the response should include the duration in minutes for each flight. 
    The response is a JSON object containing an array of flight details.
    
    :return: dict: A dictionary containing a list of flights, where each flight is represented as a dictionary with keys such as id, price, company, stops, destination, depart_iso, and arrive_iso.
    """
    return {"flights": [   
            { "id": 1, "price": 230, "company": "finnair", "stops": 0, "destination": "Paris", "depart_iso": "2026-10-15T15:00:00Z", "arrive_iso": "2026-10-15T16:05:00Z" }, 
            { "id": 2, "price": 30, "company": "air china", "stops": 0, "destination": "Beijing", "depart_iso": "2026-10-15T08:00:00Z", "arrive_iso": "2026-10-15T09:05:00Z" }, 
            { "id": 3, "price": 120, "company": "norwegian", "stops": 0, "destination": "Oslo", "depart_iso": "2026-10-15T12:00:00Z", "arrive_iso": "2026-10-15T13:15:00Z" },
            { "id": 4, "price": 185, "company": "lufthansa", "stops": 1, "destination": "Berlin", "depart_iso": "2026-10-15T10:30:00Z", "arrive_iso": "2026-10-15T12:00:00Z" },
            { "id": 5, "price": 95, "company": "lufthansa", "stops": 2, "destination": "London", "depart_iso": "2026-10-16T06:00:00Z", "arrive_iso": "2026-10-16T08:00:00Z" },
            { "id": 6, "price": 280, "company": "finnair", "stops": 0, "destination": "Paris", "depart_iso": "2026-10-16T18:00:00Z", "arrive_iso": "2026-10-16T18:55:00Z" },
            { "id": 7, "price": 150, "company": "air china", "stops": 1, "destination": "Beijing", "depart_iso": "2026-10-16T14:00:00Z", "arrive_iso": "2026-10-16T15:25:00Z" },
            { "id": 8, "price": 110, "company": "finnair", "stops": 1, "destination": "Berlin", "depart_iso": "2026-10-17T07:30:00Z", "arrive_iso": "2026-10-17T09:10:00Z" },
            { "id": 9, "price": 210, "company": "lufthansa", "stops": 0, "destination": "London", "depart_iso": "2026-10-18T16:45:00Z", "arrive_iso": "2026-10-18T17:55:00Z" },
            { "id": 10, "price": 175, "company": "norwegian", "stops": 1, "destination": "Oslo", "depart_iso": "2026-10-18T11:00:00Z", "arrive_iso": "2026-10-18T12:35:00Z" },
            { "id": 11, "price": 240, "company": "air china", "stops": 0, "destination": "Paris", "depart_iso": "2026-10-18T13:00:00Z", "arrive_iso": "2026-10-18T14:00:00Z" },
            { "id": 12, "price": 85, "company": "air china", "stops": 2, "destination": "Beijing", "depart_iso": "2026-10-18T05:00:00Z", "arrive_iso": "2026-10-18T07:20:00Z" },
            { "id": 13, "price": 195, "company": "finnair", "stops": 1, "destination": "London", "depart_iso": "2026-10-19T09:00:00Z", "arrive_iso": "2026-10-19T10:20:00Z" },
            { "id": 14, "price": 260, "company": "lufthansa", "stops": 0, "destination": "Berlin", "depart_iso": "2026-10-19T17:30:00Z", "arrive_iso": "2026-10-19T18:35:00Z" },
            { "id": 15, "price": 130, "company": "norwegian", "stops": 2, "destination": "Oslo", "depart_iso": "2026-10-20T06:30:00Z", "arrive_iso": "2026-10-20T08:20:00Z" },
            { "id": 16, "price": 220, "company": "finnair", "stops": 0, "destination": "Paris", "depart_iso": "2026-10-20T15:30:00Z", "arrive_iso": "2026-10-20T16:45:00Z" },
            { "id": 17, "price": 140, "company": "finnair", "stops": 1, "destination": "Beijing", "depart_iso": "2026-10-21T12:00:00Z", "arrive_iso": "2026-10-21T13:45:00Z" },
            { "id": 18, "price": 200, "company": "lufthansa", "stops": 0, "destination": "London", "depart_iso": "2026-10-21T14:15:00Z", "arrive_iso": "2026-10-21T15:25:00Z" },
            { "id": 19, "price": 165, "company": "finnair", "stops": 1, "destination": "Berlin", "depart_iso": "2026-10-21T10:00:00Z", "arrive_iso": "2026-10-21T11:30:00Z" },
            { "id": 20, "price": 105, "company": "norwegian", "stops": 2, "destination": "Oslo", "depart_iso": "2026-10-21T04:30:00Z", "arrive_iso": "2026-10-21T06:35:00Z" }
        ]}

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