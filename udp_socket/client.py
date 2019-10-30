import socket

LOCALHOST = '127.0.0.1'
PORT = 6789

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = raw_input()
    clientSocket.sendto(message, (LOCALHOST, PORT))
clientSocket.close()

