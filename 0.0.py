#  import socket

# client = socket.socket()
# hostname = socket.gethostname()
# port = 1234
# client.connect((hostname, port))

# name = input("name: ")
# #password = input("password: ")
# client.send(f"{name}".encode())

# data = client.recv(1024)
# print("Server sent: ", data.decode())
# while True:
#     mess = input()
#     client.send(mess.encode()) 

import socket

IP = "127.0.0.1"
PORT = 12345

client = socket.socket()
client.connect((IP, PORT))

while True:
    data = client.recv(1024).decode()
    print(data)

    msg = input()
    client.send(msg.encode())
