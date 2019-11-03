import socket

LOCALHOST = '127.0.0.1'
PORT = 6789

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client running on: ', PORT)
while True:
    message = raw_input()
    clientSocket.sendto(message, (LOCALHOST, PORT))
clientSocket.close()

