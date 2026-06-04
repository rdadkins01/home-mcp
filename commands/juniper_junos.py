def get_device_version():
    return "show version"


def get_device_logs():
    return "show log messages"


def get_device_config():
    return "show configuration"


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
    command = "show route"

    if routing_protocol and target_subnet:
        command += f" protocol {routing_protocol} {target_subnet}"
    elif target_subnet:
        command += f" {target_subnet}"
    elif routing_protocol:
        command += f" protocol {routing_protocol}"
    return command


def get_mac_address_table(
    mac_address: str=None, 
    device_interface: str=None, 
    vlan_id: str=None,
) -> str:
    command = "show ethernet-switching table"

    if mac_address:
        command += f" {mac_address}"
    elif device_interface:
        command += f" interface {device_interface}"
    elif vlan_id:
        command += f" vlan-id {vlan_id}"
    return command


def get_arp_address_table(
    vrf_name: str=None, 
    device_interface: str=None,
) -> str:
    command = "show arp no-resolve" 

    if vrf_name:
        pass # Junos doesn't require VRF to view ARP table of an interface
    if device_interface:
        command += f" interface {device_interface}"
    return command
