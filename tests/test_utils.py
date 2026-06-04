import pytest
import utils


# Fake inventory used across server tests
TEST_INVENTORY = {
    "cisco-sw": {
        "host": "192.168.10.2",
        "device_type": "cisco_ios",
        "username": "test_user",
        "password": "test_password",
    },
    "juniper-fw": {
        "host": "192.168.10.1",
        "device_type": "juniper_junos",
        "username": "test_user",
        "password": "test_password",
    },
}


# --- get_device ---

def test_get_device_returns_correct_device(monkeypatch):
    monkeypatch.setattr(utils, "INVENTORY", TEST_INVENTORY)
    result = utils.get_device("cisco-sw")
    assert result["device_type"] == "cisco_ios"
    assert result["host"] == "192.168.10.2"

def test_get_device_unknown_host_raises(monkeypatch):
    monkeypatch.setattr(utils, "INVENTORY", TEST_INVENTORY)
    with pytest.raises(ValueError, match="not found in Inventory"):
        utils.get_device("does-not-exist")

def test_get_device_error_lists_available_devices(monkeypatch):
    monkeypatch.setattr(utils, "INVENTORY", TEST_INVENTORY)
    with pytest.raises(ValueError, match="cisco-sw"):
        utils.get_device("does-not-exist")


# --- get_command ---

def test_get_command_cisco_ios():
    result = utils.get_command("get_device_version", "cisco_ios")
    assert result == "show version"

def test_get_command_juniper_junos():
    result = utils.get_command("get_device_version", "juniper_junos")
    assert result == "show version"

def test_get_command_with_kwargs():
    result = utils.get_command("get_interface_information", "cisco_ios", device_interface="GigabitEthernet0/1")
    assert result == "show interfaces GigabitEthernet0/1"

def test_get_command_unknown_key_raises():
    with pytest.raises(ValueError, match="No commands defined"):
        utils.get_command("nonexistent_command", "cisco_ios")

def test_get_command_unsupported_device_type_raises():
    with pytest.raises(ValueError, match="Unsupported device type"):
        utils.get_command("get_device_version", "arista_eos")
