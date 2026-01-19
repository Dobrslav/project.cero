import socket

client = socket.socket()
hostname = "192.168.0.107"
port = 5000
client.connect((hostname, port))
message = input(": ")
client.send(message.encode())
data = client.recv(1024)
print("server sent: ", data.decode())
client.close()