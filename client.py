import socket


client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))

user_name = input("Enter your name: ")
user_password = input("Enter your password: ")
client.send(user_name.encode())
client.send(user_password.encode())
data = client.recv(1024)

#message = input(": ")
#client.send(message.encode())

print(user_name + ":", data.decode())
client.close()