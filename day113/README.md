## TCP/IP Basics & Socket Programming Example

TCP/IP is the suite of protocols that powers the internet. Key protocols include TCP, UDP, and IP.

Below is a simple Python socket client and server example.

### Server (`tcp_server.py`):
```python
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print('Server listening...')
conn, addr = server.accept()
print('Connected by', addr)
data = conn.recv(1024)
print('Received:', data.decode())
conn.sendall(b'Hello from server!')
conn.close()
```

### Client (`tcp_client.py`):
```python
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
client.sendall(b'Hello from client!')
data = client.recv(1024)
print('Received:', data.decode())
client.close()
```

Run the server first, then the client in separate terminals.
