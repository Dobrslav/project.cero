import socket

client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))
message = input(": ")
client.send(message.encode())
data = client.recv(1024)
print("server sent: ", data.decode())
client.close()