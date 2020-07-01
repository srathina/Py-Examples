import socket

print("Hello - I am Client")


PORT = 5050
CLIENT = socket.gethostbyname(socket.gethostname())
print(socket.gethostname())
print(CLIENT)
HOST = (CLIENT, PORT)
print(HOST)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(HOST)

client.send(b"Hello world")
client.send(b"I know socket programming now")

data = client.recv(1024)
print(data)

client.close()

