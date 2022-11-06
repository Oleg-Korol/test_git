import json
import socket
from random import randint

HOST='127.0.0.1'
PORT=65432



with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))                                                   # привязывает сокет к адресу
    s.listen()                                                            # переводит сервер для приема подключений

    print('server started')

    conn,addr = s.accept()                                                 #принимает соединение.

    with conn:
        print(f'conected  by {addr}')
        while True:
            data=conn.recv(1024)                                           #получает данные из сокета.
            if data.decode().lower()=='q':
                break


            else:
                data = str(len(data))
                conn.sendall(data.encode())                                  # отправляет данные










