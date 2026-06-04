def get_device_version():
    return "show version"


def get_device_logs():
    return "show logging"


def get_device_config():
    return "show running-config"


def get_interface_information(
    device_interface: str=None,
) -> str:
    command = "show interfaces"

    if device_interface:
        command += f" {device_interface}"
    return command


def get_route_table(
    routing_protocol: str=None, 
    target_subnet: str=None,
) -> str:
    command = "show ip route"

    if target_subnet:
        command += f" {target_subnet}"
    elif routing_protocol:
        command += f" {routing_protocol}"
    return command


def get_mac_address_table(
    mac_address: str=None, 
    device_interface: str=None, 
    vlan_id: str=None,
) -> str:
    command = "show mac-address table"

    if mac_address:
        command += f" address {mac_address}"
    elif device_interface:
        command += f" interface {device_interface}"
    elif vlan_id:
        command += f" vlan {vlan_id}"
    return command


def get_arp_address_table(
    vrf_name: str=None, 
    device_interface: str=None,
) -> str:
    command = "show arp" 

    if vrf_name:
        command += f" vrf {vrf_name}"
    if device_interface:
        command += f" {device_interface}"
    return command
