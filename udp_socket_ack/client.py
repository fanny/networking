import socket
from threading import Thread
from queue import Queue

LOCALHOST = '127.0.0.1'
PORT = 6789

def wait_ack(confirmations):
    server_answer, _ = clientSocket.recvfrom(1024)
    confirmations.put(server_answer.decode('utf-8'))

def wait_data(responses):
    server_answer, _ = clientSocket.recvfrom(1024)
    responses.put(server_answer.decode('utf-8'))

def create_connection(method, arg):
    new_connection = Thread(target=method, args=(arg, ))
    new_connection.start()
    new_connection.join(timeout=2)

if __name__ == '__main__':
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    confirmations = Queue()
    responses = Queue()
    ans = ''
    result = ''
    print('Client running on: ', PORT)

    while True:
        message = input()
        clientSocket.sendto(message.encode('utf-8'), (LOCALHOST, PORT))
        
        while(not confirmations.qsize()):
            create_connection(wait_ack, confirmations)

        if confirmations.qsize():
            while(not responses.qsize()):
                print('here!')
                create_connection(wait_data, responses)
            # Returns and remove the item
            ans = confirmations.get()
            if ans == 'ACK':
                print('[SUCESS] Received ACK from server\n')
                if responses.qsize():
                    result = responses.get()
                    if result and result != 'ACK':
                        print('[SUCESS] The answer is: {}\n'.format(result))
                    else:
                        print('[ERROR] Result not received')
                else:
                    print('[ERROR] Result not received')
            else:  
                print('[ERROR] ACK not received')

    clientSocket.close()




