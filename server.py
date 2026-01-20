import socket
from _thread import *
from datetime import datetime

def client_thread(con):
    data = con.recv(1024)
    message = data.decode()
    print(f"client sent: {message}")
    con.send(message.encode())
    con.close()

server = socket.socket()
hostname = "192.168.0.255"
port = 5000
server.bind((hostname, port))
server.listen(5)

print("server starts")
while True:
    con, _ = server.accept()
    data = con.recv(1024)
    message = data.decode()
    print(f"client sent: {message}")
    con.send(message.encode())
    client, _ = server.accept()
    start_new_thread(client_thread, (client,))

