#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MCP SSE Weather Service (FastMCP Implementation)

An SSE weather service based on the FastMCP framework, declaring callable weather service tool functions via the @mcp.tool decorator.
The service provides weather data push capability via the SSE (Server-Sent Events) protocol.

Running Method:
    python weather_server_sse.py

Client Connection:
1. After starting the service, add the printed SSE endpoint to the MCP client
2. Client example code:
   mcp-client add-endpoint http://localhost:8000/sse

Development Notes:
1. Create a service instance via FastMCP("WeatherServer")
2. Declare service tool functions using the @mcp.tool decorator
3. Start the SSE service via mcp.run(transport="sse")

Dependency Installation:
    pip install fastmcp  # Install according to the actual MCP framework

Features:
• Declarative tool function registration
• Automatic SSE protocol adaptation
• Type-annotated parameter validation
• Displays client access guidance on startup

Author: [weego/WXAI-Team]
Version: 1.0.0
Last Updated: 2025-03-31
"""
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherServer")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather information for a specified region"""
    async with httpx.AsyncClient() as client:

        if not isinstance(location, str):
            raise TypeError("City name must be a string")

        key_selection = {
            "current_condition": ["temp_C", "FeelsLikeC", "humidity", "weatherDesc", "observation_time"],
        }
        try:
            resp = await client.get(f"https://wttr.in/{location}?format=j1")
            resp.raise_for_status()
            resp = resp.json()
            ret = {k: {_v: resp[k][0][_v] for _v in v} for k, v in key_selection.items()}
        except:
            import traceback
            ret = "Error encountered while fetching weather data!\n" + traceback.format_exc()

        return str(ret)


def show_client_help(host: str, port: int):
    """Display client connection help information"""
    print("\n" + "=" * 50)
    print(f"SSE service started: http://{host}:{port}")
    print("Please add the following URL to the MCP client SSE configuration:")
    print(f"\033[1;32mhttp://{host}:{port}/sse\033[0m")  # Green highlight display
    print("lightagent add lightagent_mcp_settings.json configuration example:")
    print(f"\033[1;33m    \"example-sse\": {{\n      \"url\": \"http://{host}:{port}/sse\",\n      \"disabled\": false \n   }}\033[0m")  # Yellow highlight configuration block
    print("=" * 50 + "\n")


if __name__ == "__main__":
    # Configure service parameters
    host = "0.0.0.0"  # Allow external access
    port = 8000  # Default port

    # Display client connection guidance
    show_client_help(host="localhost" if host == "0.0.0.0" else host, port=port)

    # Start SSE service (assuming FastMCP supports host/port parameters)
    mcp.run(
        transport="sse",
    )