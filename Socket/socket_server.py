import socket

print("Hello - I am Server")


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = '65.52.227.51'
print(socket.gethostname())
print(SERVER)
HOST = (SERVER, PORT)
print(HOST)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(HOST)
server.listen(1)
conn, addr = server.accept()


while True:
    data = conn.recv(2048)
    print(data)
    if data:
        conn.send(b"Received everything")
        break


conn.close()

