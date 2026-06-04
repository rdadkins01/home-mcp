from commands import cisco_ios


# --- get_device_version ---

def test_get_device_version():
    assert cisco_ios.get_device_version() == "show version"


# --- get_device_logs ---

def test_get_device_logs():
    assert cisco_ios.get_device_logs() == "show logging"


# --- get_device_config ---

def test_get_device_config():
    assert cisco_ios.get_device_config() == "show running-config"


# --- get_interface_information ---

def test_get_interface_information_no_filter():
    assert cisco_ios.get_interface_information() == "show interfaces"

def test_get_interface_information_with_filter():
    assert cisco_ios.get_interface_information("GigabitEthernet0/1") == "show interfaces GigabitEthernet0/1"


# --- get_route_table ---

def test_get_route_table_no_args():
    assert cisco_ios.get_route_table() == "show ip route"

def test_get_route_table_with_subnet():
    assert cisco_ios.get_route_table(target_subnet="10.0.0.0/24") == "show ip route 10.0.0.0/24"

def test_get_route_table_with_protocol():
    assert cisco_ios.get_route_table(routing_protocol="ospf") == "show ip route ospf"

def test_get_route_table_subnet_takes_priority_over_protocol():
    # When both are provided, target_subnet takes priority
    assert cisco_ios.get_route_table(routing_protocol="ospf", target_subnet="10.0.0.0/24") == "show ip route 10.0.0.0/24"


# --- get_mac_address_table ---

def test_get_mac_address_table_no_filter():
    assert cisco_ios.get_mac_address_table() == "show mac-address table"

def test_get_mac_address_table_with_mac():
    assert cisco_ios.get_mac_address_table(mac_address="aa:bb:cc:dd:ee:ff") == "show mac-address table address aa:bb:cc:dd:ee:ff"

def test_get_mac_address_table_with_interface():
    assert cisco_ios.get_mac_address_table(device_interface="GigabitEthernet0/1") == "show mac-address table interface GigabitEthernet0/1"

def test_get_mac_address_table_with_vlan():
    assert cisco_ios.get_mac_address_table(vlan_id="10") == "show mac-address table vlan 10"

def test_get_mac_address_table_mac_takes_priority_over_interface():
    # mac_address takes priority when multiple filters provided
    assert cisco_ios.get_mac_address_table(mac_address="aa:bb:cc:dd:ee:ff", device_interface="GigabitEthernet0/1") == "show mac-address table address aa:bb:cc:dd:ee:ff"


# --- get_arp_address_table ---

def test_get_arp_address_table_no_filter():
    assert cisco_ios.get_arp_address_table() == "show arp"

def test_get_arp_address_table_with_vrf():
    assert cisco_ios.get_arp_address_table(vrf_name="MGMT") == "show arp vrf MGMT"

def test_get_arp_address_table_with_interface():
    assert cisco_ios.get_arp_address_table(device_interface="GigabitEthernet0/1") == "show arp GigabitEthernet0/1"

def test_get_arp_address_table_with_vrf_and_interface():
    assert cisco_ios.get_arp_address_table(vrf_name="MGMT", device_interface="GigabitEthernet0/1") == "show arp vrf MGMT GigabitEthernet0/1"
