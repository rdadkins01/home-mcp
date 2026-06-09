import yaml, os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from commands import COMMANDS


load_dotenv()

with open("inventory.yaml") as file:
    INVENTORY = yaml.safe_load(file)["devices"]


for device in INVENTORY.values():
    device["username"] = os.environ["MCP_USERNAME"]
    device["password"] = os.environ["MCP_PASSWORD"]


def get_device(host_name: str) -> dict:
    if host_name not in INVENTORY:
        raise ValueError(f"{host_name} not found in Inventory. Available: {list(INVENTORY.keys())}")
    return INVENTORY[host_name]


def get_command(command_key: str, device_type: str, **kwargs) -> str:
    if command_key not in COMMANDS:
        raise ValueError(f"No commands defined for '{command_key}")
    if device_type not in COMMANDS[command_key]:
        raise ValueError(f"Unsupported device type: {device_type}")
    return COMMANDS[command_key][device_type](**kwargs)


def send_command(host_info: dict, command: str) -> str:
    with ConnectHandler(**host_info) as ssh_session:
        return ssh_session.send_command(command)