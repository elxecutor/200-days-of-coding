import os
import re

def get_ethernet_interfaces():
    interfaces = []
    try:
        with open('/proc/net/dev', 'r') as f:
            data = f.read()
        for line in data.splitlines()[2:]:
            iface = line.split(':')[0].strip()
            # Common Ethernet interface names: eth0, enp*, eno*
            if re.match(r'^(eth\d+|enp\d+|eno\d+)$', iface):
                interfaces.append(iface)
    except Exception as e:
        print(f"Error reading interfaces: {e}")
    return interfaces

def check_link_status(iface):
    carrier_path = f"/sys/class/net/{iface}/carrier"
    try:
        with open(carrier_path, 'r') as f:
            status = f.read().strip()
        return status == '1'
    except Exception:
        return False

def main():
    interfaces = get_ethernet_interfaces()
    if not interfaces:
        print("No Ethernet interfaces found.")
        return
    for iface in interfaces:
        status = check_link_status(iface)
        print(f"Interface {iface}: {'Connected' if status else 'Disconnected'}")

if __name__ == "__main__":
    main()
