# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2,<3",
#     "mcp>=1.2.0,<2",
# ]
# ///

import sys
import requests

from mcp.server.fastmcp import FastMCP

DEFAULT_X64DBG_SERVER = "http://127.0.0.1:8888/"
x64dbg_server_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_X64DBG_SERVER

mcp = FastMCP("x64dbg-mcp")

def safe_get(endpoint: str, params: dict = None) -> list:
    """
    Perform a GET request with optional query parameters.
    """
    if params is None:
        params = {}

    url = f"{x64dbg_server_url}/{endpoint}"

    try:
        response = requests.get(url, params=params, timeout=5)
        response.encoding = 'utf-8'
        if response.ok:
            return response.text.splitlines()
        else:
            return [f"Error {response.status_code}: {response.text.strip()}"]
    except Exception as e:
        return [f"Request failed: {str(e)}"]

def safe_post(endpoint: str, data: dict | str) -> str:
    try:
        if isinstance(data, dict):
            response = requests.post(f"{x64dbg_server_url}/{endpoint}", data=data, timeout=5)
        else:
            response = requests.post(f"{x64dbg_server_url}/{endpoint}", data=data.encode("utf-8"), timeout=5)
        response.encoding = 'utf-8'
        if response.ok:
            return response.text.strip()
        else:
            return f"Error {response.status_code}: {response.text.strip()}"
    except Exception as e:
        return f"Request failed: {str(e)}"

@mcp.tool()
def Is_Debugging(Dbgcheck: str) -> str:
    """
    Find if currently debugging
    """
    return safe_get("IsDebugActive", {"dbgcheck": Dbgcheck})

@mcp.tool()
def ExeConsoleCmd(Command: str) -> list:
    """
    Execute a console command
    """
    return safe_get("ExeConsoleCmd", {"Command": Command})

if __name__ == "__main__":
    mcp.run()