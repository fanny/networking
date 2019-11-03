import socket
from threading import Thread
from queue import Queue

LOCALHOST = '127.0.0.1'
PORT = 6789

def wait_ack(confirmations):
    server_answer, _ = clientSocket.recvfrom(1024)
    confirmations.put(server_answer.decode('utf-8'))

if __name__ == '__main__':
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    confirmations = Queue()
    print('Client running on: ', PORT)

    while True:
        message = input()
        clientSocket.sendto(message.encode('utf-8'), (LOCALHOST, PORT))
        
        new_connection = Thread(target=wait_ack, args=(confirmations, ))
        new_connection.start()
        new_connection.join(timeout=2)

        if(confirmations.qsize()):
            # Returns and remove the item
            ans = confirmations.get()
            if ans == 'ACK':
                result, _ = clientSocket.recvfrom(1024)
                print('Receveid  ACK  from server')
                print('\n The Answer is: {}'.format(result.decode('utf-8')))
        else:
            print('ACK NOT RECEIVED! :(')
    clientSocket.close()




