# Basics of Computer Networking  
## The Bits and Bytes of Computer Networking

This document provides a quick overview of essential computer networking concepts and practical commands, as demonstrated in the accompanying `main.sh` script.

---

## Key Networking Tasks

### 1. Check Your IP Address
To view your device's IP addresses, use:
```bash
ip addr show | grep 'inet '
```
This command lists all network interfaces and their assigned IP addresses.

### 2. Test Network Connectivity
To verify if your system can reach the internet, use:
```bash
ping -c 4 google.com
```
This sends 4 ICMP echo requests to `google.com` and displays the results.

### 3. Display Routing Table
To see how your system routes network traffic, use:
```bash
ip route
```
This shows the current routing table, including default gateways and network destinations.

### 4. List Open Network Ports
To check which ports are open and listening for connections, use:
```bash
ss -tuln
```
This displays all TCP and UDP sockets in listening mode.

---

## Summary

Understanding these basic commands helps you diagnose and troubleshoot network issues, monitor connectivity, and manage your system's network configuration.

For hands-on practice, refer to the `main.sh` script in this directory.