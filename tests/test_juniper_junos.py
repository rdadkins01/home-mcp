from commands import juniper_junos


# --- get_device_version ---

def test_get_device_version():
    assert juniper_junos.get_device_version() == "show version"


# --- get_device_logs ---

def test_get_device_logs():
    assert juniper_junos.get_device_logs() == "show log messages"


# --- get_device_config ---

def test_get_device_config():
    assert juniper_junos.get_device_config() == "show configuration"


# --- get_interface_information ---

def test_get_interface_information_no_filter():
    assert juniper_junos.get_interface_information() == "show interfaces"

def test_get_interface_information_with_filter():
    assert juniper_junos.get_interface_information("ge-0/0/0") == "show interfaces ge-0/0/0"


# --- get_route_table ---

def test_get_route_table_no_args():
    assert juniper_junos.get_route_table() == "show route"

def test_get_route_table_with_subnet():
    assert juniper_junos.get_route_table(target_subnet="10.0.0.0/24") == "show route 10.0.0.0/24"

def test_get_route_table_with_protocol():
    assert juniper_junos.get_route_table(routing_protocol="ospf") == "show route protocol ospf"

def test_get_route_table_with_both_protocol_and_subnet():
    # Junos supports both simultaneously
    assert juniper_junos.get_route_table(routing_protocol="ospf", target_subnet="10.0.0.0/24") == "show route protocol ospf 10.0.0.0/24"


# --- get_mac_address_table ---

def test_get_mac_address_table_no_filter():
    assert juniper_junos.get_mac_address_table() == "show ethernet-switching table"

def test_get_mac_address_table_with_mac():
    assert juniper_junos.get_mac_address_table(mac_address="aa:bb:cc:dd:ee:ff") == "show ethernet-switching table aa:bb:cc:dd:ee:ff"

def test_get_mac_address_table_with_interface():
    assert juniper_junos.get_mac_address_table(device_interface="ge-0/0/0") == "show ethernet-switching table interface ge-0/0/0"

def test_get_mac_address_table_with_vlan():
    assert juniper_junos.get_mac_address_table(vlan_id="10") == "show ethernet-switching table vlan-id 10"

def test_get_mac_address_table_mac_takes_priority_over_interface():
    assert juniper_junos.get_mac_address_table(mac_address="aa:bb:cc:dd:ee:ff", device_interface="ge-0/0/0") == "show ethernet-switching table aa:bb:cc:dd:ee:ff"


# --- get_arp_address_table ---

def test_get_arp_address_table_no_filter():
    assert juniper_junos.get_arp_address_table() == "show arp no-resolve"

def test_get_arp_address_table_with_interface():
    assert juniper_junos.get_arp_address_table(device_interface="ge-0/0/0") == "show arp no-resolve interface ge-0/0/0"

def test_get_arp_address_table_vrf_ignored():
    # Junos doesn't use VRF in this command — result should be same as no filter
    assert juniper_junos.get_arp_address_table(vrf_name="MGMT") == "show arp no-resolve"
