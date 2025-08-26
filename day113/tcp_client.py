import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))
client.sendall(b'Hello from client!')
data = client.recv(1024)
print('Received:', data.decode())
client.close()
