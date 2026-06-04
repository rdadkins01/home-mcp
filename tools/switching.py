from fastmcp import FastMCP
from utils import get_device, get_command, send_command


mcp = FastMCP("home-network")


# Tools
@mcp.tool()
def get_interface_information(
    device_name: str, 
    device_interface: str = None,
) -> str:
    '''Get information about a device's ports/interfaces.

    Args:
        device_name: Name of the device being queried.
        device_interface: Optional interface filter.
    '''
    host_info = get_device(device_name)
    command = get_command(
        command_key = "get_interface_information", 
        device_type = host_info["device_type"], 
        device_interface = device_interface,
    )
    return send_command(host_info, command)


@mcp.tool()
def get_mac_address_table(
    device_name: str, 
    mac_address: str = None, 
    device_interface: str = None,
    vlan_id: str = None,
) -> str:
    '''Get MAC address table for a device.

    Args:
        device_name: Name of the device being queried.
        mac_address: Optional MAC address filter.
        device_interface: Optional device interface filter.
        vlan_id: Optional VLAN ID filter.
    '''
    host_info = get_device(device_name)
    command = get_command(
        command_key="get_mac_address_table", 
        device_type=host_info["device_type"],
        mac_address=mac_address,
        device_interface=device_interface,
        vlan_id=vlan_id,
    )
    return send_command(host_info, command)


@mcp.tool()
def get_arp_address_table(
    device_name: str,
    vrf_name: str = None,
    device_interface: str = None,
) -> str:
    '''Get ARP table for a device.

    Args:
        device_name: Name of the device being queried.
        vrf_name: Optional VRF selection for the ARP table.
        device_interface: Optional device interface.
    '''
    host_info = get_device(device_name)
    command = get_command(
        command_key="get_arp_address_table", 
        device_type=host_info["device_type"],
        vrf_name=vrf_name,
        device_interface=device_interface,
    )
    return send_command(host_info, command)