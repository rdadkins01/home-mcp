from fastmcp import FastMCP
from utils import get_device, get_command, send_command


mcp = FastMCP("home-network")

 
# Tools
@mcp.tool()
def get_device_version(device_name: str) -> str:
    '''Get hardware and software version information for a device.

    Args:
        device_name: The name of the device being queried.
    '''
    host_info = get_device(device_name)
    command = get_command(
        command_key = "get_device_version", 
        device_type = host_info["device_type"],
    )
    return send_command(host_info, command)


@mcp.tool()
def get_device_logs(
    device_name: str,
) -> str:
    '''Get system logs for a device.

    Args:
        device_name: Name of the device being queried.
    '''
    host_info = get_device(device_name)
    command = get_command(
        command_key="get_device_logs", 
        device_type=host_info["device_type"]
    )
    return send_command(host_info, command)


@mcp.tool()
def get_device_config(
    device_name: str,
) -> str:
    '''Get the configuration for a device.

    Args:
        device_name: Name of the device being queried.
    '''
    host_info = get_device(device_name)
    command = get_command(
        command_key="get_device_config", 
        device_type=host_info["device_type"]
    )
    return send_command(host_info, command)