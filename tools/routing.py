from fastmcp import FastMCP
from utils import get_device, get_command, send_command


mcp = FastMCP("home-network")


# Tools
@mcp.tool()
def get_route_table(
    device_name: str, 
    routing_protocol: str = None, 
    target_subnet: str = None,
) -> str:
    '''Get route table for a device.

    Args:
        device_name: Name of the device being queried.
        routing_protocol: The routing protocol to query on.
        target_subnet: The subnet or host that to check the routing table for.
    '''
    host_info = get_device(device_name)
    command = get_command(
        command_key = "get_route_table", 
        device_type = host_info["device_type"], 
        routing_protocol = routing_protocol, 
        target_subnet = target_subnet,
    )
    return send_command(host_info, command)