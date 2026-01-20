import socket

client = socket.socket(socket.gethostname(), 5000)
socket.connect()
client.close()
