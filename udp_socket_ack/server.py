# -*- coding: utf-8 -*- 
import socket

LOCALHOST = '127.0.0.1'
PORT = 6789

def calculator(operation, first_number, second_number):
    result = 'Operação não cadastrada, pena.'
    first_number = int(first_number)
    second_number = int(second_number) 
    if operation == 'ADD':
        result = first_number + second_number
    elif operation == 'SUB':
        result = first_number - second_number
    elif operation == 'MULT':
        result = first_number * second_number
    elif operation == 'EXP':
        result = first_number ** second_number
    elif operation == 'DIV ' and second_number != 0:
        result = first_number / second_number

    return result

def handle_connection():
    data, addr = serverSocket.recvfrom(1024)
    operation, first_number, second_number = data.split(' ')
    
    serverSocket.sendto('ACK', addr)
    serverSocket.sendto(calculator(operation, first_number, second_number), addr)

if __name__ == '__main__':
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((LOCALHOST, PORT))
    print('Server listening on: ', PORT)
    
    while True:
        new_connection = Thread(target=handle_connection)
        new_connection.start()
    serverSocket.close()