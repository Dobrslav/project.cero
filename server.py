import socket
from datetime import datetime

server = socket.socket()
hostname = socket.gethostname()
port = 12345
server.bind((hostname, port))
server.listen(5)

print("server starts")
while True:
    con, _ = server.accept()
    data = con.recv(1024)
    message = data.decode()
    print(f"client sent: {message}")
    con.send(message.encode())
    con.close()

