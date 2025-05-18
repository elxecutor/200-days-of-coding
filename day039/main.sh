#!/bin/bash

echo "6. Check your IP address:"
ip addr show | grep 'inet '

echo
echo "7. Test network connectivity (ping google.com):"
ping -c 4 google.com

echo
echo "8. Display routing table:"
ip route

echo
echo "9. List open network ports:"
ss -tuln
