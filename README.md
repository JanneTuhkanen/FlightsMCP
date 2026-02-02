# Template MCP Server Project

A template project to jump-start your MCP (Model Context Protocol) server development using FastMCP.

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. MCP provides a standardized way to expose tools, resources, and prompts to AI models.

This template provides a FastMCP-based server implementation with a simple health check tool to get you started quickly.

## Features

- 🚀 Built with [FastMCP](https://github.com/jlowin/fastmcp) for easy MCP server development
- 🔧 Pre-configured with a health check tool
- 🌐 CORS middleware support for web clients
- 📝 Environment-based configuration
- ✅ Testing setup with pytest

## Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip

## Setup

### 1. Install Dependencies

Using uv (recommended):
```bash
uv pip install -r requirements.txt
```

Or using pip:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy the example environment file to create your working configuration:

```bash
# On Windows (PowerShell)
Copy-Item .env.example .env

# On macOS/Linux
cp .env.example .env
```

Edit the `.env` file to customize your settings:
```env
APP_VERSION="0.0.1"
```

## Running the Server

Start the MCP server:

```bash
uv run uvicorn app.main:app --port [PORT]

```
See ```start_server.sh```

The server will start and be available for MCP client connections. By default, it includes:
- A health check tool that returns the server status, version, and uptime

## Testing

This project uses pytest for testing. Run the test suite:

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run a specific test file
uv run pytest tests/test_example.py
```

## MCP Documentation

### About the Model Context Protocol

MCP enables LLM applications to:
- **Access Tools**: Expose callable functions that the LLM can invoke
- **Retrieve Resources**: Provide access to data sources and documents
- **Use Prompts**: Share reusable prompt templates
- **Sample**: Request LLM completions from the server

### Key Concepts

- **Server**: Exposes tools, resources, and prompts (this template)
- **Client**: Connects to servers and uses their capabilities (like Claude Desktop, IDEs)
- **Transport**: Communication layer between client and server (stdio, HTTP, SSE)

### Available Tools

This template includes one example tool:

    health()
    Returns the current status of the MCP server.


### Adding Your Own Tools

To add new tools, use the `@mcp.tool()` decorator in [app/main.py](app/main.py):

```python
@mcp.tool()
async def my_custom_tool(param: str) -> dict:
    """Description of what your tool does."""
    # Your tool implementation
    return {"result": "success"}
```