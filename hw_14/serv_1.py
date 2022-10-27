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
            if data.decode()=='q' or data.decode()=="Q":
                break

            elif data.decode()=='auth':
                token=f'token:<some_unic_token>'
                conn.sendall(token.encode())
                with open("data_file.json", "w") as write_file:
                    json.dump(token, write_file)

            else:
                data = str(len(data))
                conn.sendall(data.encode())                                  # отправляет данные










