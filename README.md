# home-mcp

A Model Context Protocol (MCP) server for querying home network devices. It uses [FastMCP](https://github.com/jlowin/fastmcp) and [Netmiko](https://github.com/ktbyers/netmiko) to SSH into routers and switches and return structured output to any MCP-compatible client (e.g. Claude Desktop, Claude Code).

## Supported Device Types

| Vendor | `device_type` value |
|---|---|
| Cisco IOS / IOS-XE | `cisco_ios` |
| Juniper JunOS | `juniper_junos` |

## Available Tools

### System
| Tool | Description |
|---|---|
| `get_device_version` | Hardware and software version info |
| `get_device_logs` | System log output |
| `get_device_config` | Full running/active configuration |

### Routing
| Tool | Description |
|---|---|
| `get_route_table` | Route table, optionally filtered by protocol or subnet |

### Switching
| Tool | Description |
|---|---|
| `get_interface_information` | Interface status and statistics, optionally filtered by interface |
| `get_mac_address_table` | MAC address table, optionally filtered by MAC, interface, or VLAN |
| `get_arp_address_table` | ARP table, optionally filtered by VRF or interface |

---

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- SSH access to your network devices

### Install

```bash
git clone https://github.com/rdadkins01/home-mcp.git
cd home-mcp
uv sync
```

---

## Configuration

### Credentials — `.env`

The server reads a single set of SSH credentials from a `.env` file in the project root. These credentials are injected into every device connection at startup.

Copy the example and fill in your values:

```bash
cp .env.example .env
```

`.env.example`:
```env
MCP_USERNAME=
MCP_PASSWORD=
```

**Both fields are required.** The server will raise a `KeyError` at startup if either is missing from the environment.

> `.env` is listed in `.gitignore` and will never be committed to the repository.

---

### Inventory — `inventory.yaml`

The inventory file defines every device the MCP server can reach. It is loaded once at startup and must exist before the server runs.

Copy the example and add your devices:

```bash
cp inventory.yaml.example inventory.yaml
```

`inventory.yaml.example`:
```yaml
devices:
  example-device:
    host: 192.168.x.x
    device_type: cisco_ios
```

**Schema:**

```yaml
devices:
  <device-name>:          # Arbitrary name — used as the device_name argument in all tools
    host: <ip-or-fqdn>   # IP address or hostname reachable over SSH
    device_type: <type>  # One of: cisco_ios, juniper_junos
```

You can add as many devices as needed:

```yaml
devices:
  core-router:
    host: 192.168.1.1
    device_type: cisco_ios
  edge-switch:
    host: 192.168.1.2
    device_type: cisco_ios
  firewall:
    host: 192.168.1.254
    device_type: juniper_junos
```

The `username` and `password` fields are **not** stored in the inventory file — they are injected automatically from `.env` at runtime.

> `inventory.yaml` is listed in `.gitignore` and will never be committed to the repository.

---

## Running the Server

```bash
uv run python server.py
```

The server starts in stdio mode by default, which is how MCP clients communicate with it.

---

## Connecting to Claude Desktop / Claude Code

Add the server to your MCP client configuration. Example for Claude Desktop (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "home-network": {
      "command": "uv",
      "args": ["run", "python", "server.py"],
      "cwd": "/path/to/home-mcp"
    }
  }
}
```

---

## Project Structure

```
home-mcp/
├── server.py               # Entry point — mounts all tool groups
├── utils.py                # Inventory loader, credential injector, SSH helper
├── inventory.yaml          # Your device inventory (git-ignored)
├── inventory.yaml.example  # Template for inventory.yaml
├── .env                    # Your credentials (git-ignored)
├── .env.example            # Template for .env
├── commands/
│   ├── __init__.py         # COMMANDS dispatch table
│   ├── cisco_ios.py        # Cisco IOS command builders
│   └── juniper_junos.py    # Juniper JunOS command builders
├── tools/
│   ├── system.py           # System tools (version, logs, config)
│   ├── routing.py          # Routing tools (route table)
│   └── switching.py        # Switching tools (interfaces, MAC, ARP)
└── tests/
    ├── test_cisco_ios.py
    ├── test_juniper_junos.py
    └── test_utils.py
```

---

## Running Tests

```bash
uv run pytest
```
