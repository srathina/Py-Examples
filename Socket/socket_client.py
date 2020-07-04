import socket

print("Hello - I am Client")


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = '65.52.227.51'
print(socket.gethostname())
print(SERVER)
HOST = (SERVER, PORT)
print(HOST)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(HOST)

client.send(b'Hello')
client.send(b'I know socket programming now')

data = client.recv(2048)
print(data)

client.close()

