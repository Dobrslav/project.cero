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
    client, addr = server.accept() #_
    start_new_thread(client_thread, (client, addr))

#надо придумать проверку логина и пароля