from . import cisco_ios, juniper_junos

COMMANDS = {
    "get_device_version": {
        "cisco_ios": cisco_ios.get_device_version,
        "juniper_junos": juniper_junos.get_device_version,
    },
    "get_interface_information": {
        "cisco_ios": cisco_ios.get_interface_information,
        "juniper_junos": juniper_junos.get_interface_information,
    },
    "get_route_table": {
        "cisco_ios": cisco_ios.get_route_table,
        "juniper_junos": juniper_junos.get_route_table
    },
    "get_mac_address_table": {
        "cisco_ios": cisco_ios.get_mac_address_table,
        "juniper_junos": juniper_junos.get_mac_address_table,
    },
    "get_arp_address_table": {
        "cisco_ios": cisco_ios.get_arp_address_table,
        "juniper_junos": juniper_junos.get_arp_address_table,
    },
    "get_device_logs": {
        "cisco_ios": cisco_ios.get_device_logs,
        "juniper_junos": juniper_junos.get_device_logs,
    },
    "get_device_config": {
        "cisco_ios": cisco_ios.get_device_config,
        "juniper_junos": juniper_junos.get_device_config,
    },
}