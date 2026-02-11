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

@mcp.tool("flights")
async def get_flights() -> dict:
    """
    Docstring for get_flights tool. This tool returns a list of available flights with details such as price, company, stops, and departure/arrival times in ISO format.
    Duration should be calculated from the departure and arrival times upon receiving the request, and the response should include the duration in minutes for each flight. 
    The response is a JSON object containing an array of flight details.
    
    :return: dict: A dictionary containing a list of flights, where each flight is represented as a dictionary with keys such as id, price, company, stops, destination, depart_iso, and arrive_iso.
    Format of the json response: {"flights": [ { "id": int, "price": int, "company": str, "stops": int, "destination": str, "depart_iso": str, "arrive_iso": str }, ... ]}
    """
    flights_data = [   
        { "id": 1, "destination": "Paris", "company": "finnair", "stops": 0, "depart_iso": "2026-10-15T15:00:00Z", "arrive_iso": "2026-10-15T16:05:00Z", "price": 230 }, 
        { "id": 2, "destination": "Beijing", "company": "air china", "stops": 0, "depart_iso": "2026-10-15T08:00:00Z", "arrive_iso": "2026-10-15T09:05:00Z", "price": 30 }, 
        { "id": 3, "destination": "Oslo", "company": "norwegian", "stops": 0, "depart_iso": "2026-10-15T12:00:00Z", "arrive_iso": "2026-10-15T13:15:00Z", "price": 120 },
        { "id": 4, "destination": "Berlin", "company": "lufthansa", "stops": 1, "depart_iso": "2026-10-15T10:30:00Z", "arrive_iso": "2026-10-15T12:00:00Z", "price": 185 },
        { "id": 5, "destination": "London", "company": "lufthansa", "stops": 2, "depart_iso": "2026-10-16T06:00:00Z", "arrive_iso": "2026-10-16T08:00:00Z", "price": 95 },
        { "id": 6, "destination": "Paris", "company": "finnair", "stops": 0, "depart_iso": "2026-10-16T18:00:00Z", "arrive_iso": "2026-10-16T18:55:00Z", "price": 280 },
        { "id": 7, "destination": "Beijing", "company": "air china", "stops": 1, "depart_iso": "2026-10-16T14:00:00Z", "arrive_iso": "2026-10-16T15:25:00Z", "price": 150 },
        { "id": 8, "destination": "Berlin", "company": "finnair", "stops": 1, "depart_iso": "2026-10-17T07:30:00Z", "arrive_iso": "2026-10-17T09:10:00Z", "price": 110 },
        { "id": 9, "destination": "London", "company": "lufthansa", "stops": 0, "depart_iso": "2026-10-18T16:45:00Z", "arrive_iso": "2026-10-18T17:55:00Z", "price": 210 },
        { "id": 10, "destination": "Oslo", "company": "norwegian", "stops": 1, "depart_iso": "2026-10-18T11:00:00Z", "arrive_iso": "2026-10-18T12:35:00Z", "price": 175 },
        { "id": 11, "destination": "Paris", "company": "air china", "stops": 0, "depart_iso": "2026-10-18T13:00:00Z", "arrive_iso": "2026-10-18T14:00:00Z", "price": 240 },
        { "id": 12, "destination": "Beijing", "company": "air china", "stops": 2, "depart_iso": "2026-10-18T05:00:00Z", "arrive_iso": "2026-10-18T07:20:00Z", "price": 85 },
        { "id": 13, "destination": "London", "company": "finnair", "stops": 1, "depart_iso": "2026-10-19T09:00:00Z", "arrive_iso": "2026-10-19T10:20:00Z", "price": 195 },
        { "id": 14, "destination": "Berlin", "company": "lufthansa", "stops": 0, "depart_iso": "2026-10-19T17:30:00Z", "arrive_iso": "2026-10-19T18:35:00Z", "price": 260 },
        { "id": 15, "destination": "Oslo", "company": "norwegian", "stops": 2, "depart_iso": "2026-10-20T06:30:00Z", "arrive_iso": "2026-10-20T08:20:00Z", "price": 130 },
        { "id": 16, "destination": "Paris", "company": "finnair", "stops": 0, "depart_iso": "2026-10-20T15:30:00Z", "arrive_iso": "2026-10-20T16:45:00Z", "price": 220 },
        { "id": 17, "destination": "Beijing", "company": "finnair", "stops": 1, "depart_iso": "2026-10-21T12:00:00Z", "arrive_iso": "2026-10-21T13:45:00Z", "price": 140 },
        { "id": 18, "destination": "London", "company": "lufthansa", "stops": 0, "depart_iso": "2026-10-21T14:15:00Z", "arrive_iso": "2026-10-21T15:25:00Z", "price": 200 },
        { "id": 19, "destination": "Berlin", "company": "finnair", "stops": 1, "depart_iso": "2026-10-21T10:00:00Z", "arrive_iso": "2026-10-21T11:30:00Z", "price": 165 },
        { "id": 20, "destination": "Oslo", "company": "norwegian", "stops": 2, "depart_iso": "2026-10-21T04:30:00Z", "arrive_iso": "2026-10-21T06:35:00Z", "price": 105 }
    ]
    
    return {"flights": flights_data}

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