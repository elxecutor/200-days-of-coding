import os
import re

def get_wifi_interfaces():
    interfaces = []
    try:
        with open('/proc/net/wireless', 'r') as f:
            data = f.read()
        for line in data.splitlines()[2:]:
            iface = line.split()[0].strip(':')
            interfaces.append(iface)
    except Exception as e:
        print(f"Error reading wireless interfaces: {e}")
    return interfaces

def check_wifi_status(iface):
    operstate_path = f"/sys/class/net/{iface}/operstate"
    try:
        with open(operstate_path, 'r') as f:
            status = f.read().strip()
        return status == 'up'
    except Exception:
        return False

def main():
    interfaces = get_wifi_interfaces()
    if not interfaces:
        print("No Wi-Fi interfaces found.")
        return
    for iface in interfaces:
        status = check_wifi_status(iface)
        print(f"Interface {iface}: {'Connected' if status else 'Disconnected'}")

if __name__ == "__main__":
    main()
