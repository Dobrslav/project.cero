# import socket
# from _thread import*

# password_list = {"admin": "1234", "user": "abcd"}  #логин и пароль
# logmess = []

# def client_thread(con):         #данные от клиента
#     data = con.recv(1024)
#     message = data.decode()
#     print(f"client name: {message}")
#     if message in password_list:
#         con.send(f"Welcome, {message}!".encode())
#         dat = con.recv(1024)
#         mes = dat.decode()
#         logmess.append(mes)
#         con.send(f"{message}, : {mes}".encode())
#     else:
#         con.send("Access denied.".encode())
#         con.close()
    
    

# server = socket.socket()        #тело сервера
# hostname = socket.gethostname()
# port = 1234
# server.bind((hostname, port))
# server.listen(5)

# print("server starts") #много поточность клиентов
# while True:
#             client, _ = server.accept()
#             start_new_thread(client_thread, (client, ))


import os
import socket
from _thread import start_new_thread

from pyparsing import line

server = socket.socket()
hostname = "0.0.0.0"
port = 12345
server.bind((hostname, port))
server.listen(5)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
users_file = os.path.join(BASE_DIR, "users.txt")

def load_users():
    users = {}
    if not os.path.exists(users_file):
        open(users_file, "w", encoding="utf-8").close()
        return users
    with open(users_file, "r", encoding="utf-8") as file:
        for line in file:
            if ":" in line:
                username, password = line.strip().split(":", 1)
                users[username] = password
    return users

def save_user(login, password):
    with open(users_file, "a", encoding="utf-8") as file:
        file.write(f"{login}:{password}\n")

def client_thread(conn, addr):
    users = load_users()
    try:
        conn.send("Login: ".encode())
        login = conn.recv(1024).decode().strip()

        conn.send("Password: ".encode())
        password = conn.recv(1024).decode().strip()

        if login in users and users[login] == password:
            conn.send("Access granted\n".encode())

        elif login not in users:
            users[login] = password
            save_user(login, password)
            conn.send("New user registered. Access granted\n".encode())
        else:
            conn.send("Access denied\n".encode())
            conn.close()
            return

        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            #print(f"{login}: {msg.decode()}")
            #conn.send(f"Echo: {msg.decode()}".encode())

    except:
        pass
    finally:
        conn.close()

print("Server started")

while True:
    client, addr = server.accept()
    start_new_thread(client_thread, (client, addr))