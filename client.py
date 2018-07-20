import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('52.78.104.59', 12345))

inp = input()

sock.send(inp.encode())
data = sock.recv(65535)

print(data.decode())
