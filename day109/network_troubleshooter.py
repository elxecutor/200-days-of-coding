import subprocess
import socket
import os

def ping_test(host="8.8.8.8"):
    print(f"Pinging {host}...")
    try:
        result = subprocess.run(["ping", "-c", "2", host], capture_output=True, text=True)
        print(result.stdout)
        return result.returncode == 0
    except Exception as e:
        print(f"Ping error: {e}")
        return False

def dns_test(domain="google.com"):
    print(f"Resolving DNS for {domain}...")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolved to {ip}")
        return True
    except Exception as e:
        print(f"DNS error: {e}")
        return False

def get_default_gateway():
    print("Getting default gateway...")
    try:
        with open("/proc/net/route") as f:
            for line in f.readlines():
                fields = line.strip().split()
                if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                    continue
                gw = socket.inet_ntoa(bytes.fromhex(fields[2])[::-1])
                print(f"Default gateway: {gw}")
                return gw
    except Exception as e:
        print(f"Gateway error: {e}")
    return None

def main():
    ping_test()
    dns_test()
    get_default_gateway()

if __name__ == "__main__":
    main()
