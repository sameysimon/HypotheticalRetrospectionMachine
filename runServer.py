import socket
import Environment

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while(True):
    clientSocket, address = s.accept()
    print(f"Connection from address, {address} has been establshed.")
    clientSocket.send(bytes("Welcome to the Server", "utf-8"))

 