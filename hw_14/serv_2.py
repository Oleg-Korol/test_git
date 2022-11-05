# Ex.2
# Добавить в Ex.1 аутентификацию.
# Клиент отправляет серверу строку 'auth'. Сервер возвращает клиенту строку с уникальным токеном вида
# 'token:<some_unic_token>'.
# Доработать сервер, чтобы он из принятой строки получал json.
# Клиент при отправке "боевого запроса" добавляет в json данный токен.
#
# Пример запроса клиента json-строка
# '{'token': <some_unic_token>, 'data': 'some text data'}'
#
# Пример ответа сервера
# '{'token': <some_unic_token>, 'length': <data_length>}'
#
# Клиет, которому уже был выдан токен, при повторном запросе должен использовать тот же токен.
# Реализовать логиру проверки на стороне сервера. При повторном запросе 'auth' - выдавать тот же токен.





# Не понял как это реализовать.Пытался сделать что то похожее.
#
# Идея была следующая:
# Когда клиент отправляет серверу строку 'auth' в первый раз -  сервер генерирует условно уникальный токен и записывает ip клиента в список .
# Возвращает клиенту строку с уникальным токеном, а значение токена записывает в json файл ключом которого явлется IP адресс клиента
# При повторном отправлении клиентом 'auth', сервер проверяет на наличие данного ip в списке.
# Если его нет, то генерирует новый, а если находит, то достает из json  по IP токен клиента и возвращает ему.





import json
import socket
from random import randint





HOST='127.0.0.1'
PORT=65472

keys=[]

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

            elif data.decode()=='auth':
                if HOST in keys:
                    with open("data_file.json", "r") as rd:
                        baza = json.load(rd)
                        for k, v in baza.items():
                            if k == HOST:
                                conn.sendall(v.encode())

                else:
                    number=randint(1,1000)
                    token_client=(f'{HOST}:<some_unic_token{number}')
                    token={f'{HOST}':f'some_unic_token{number}'}
                    keys.append(HOST)
                    conn.sendall(token_client.encode())
                    with open("data_file.json", "w") as write_file:
                         json.dump(token, write_file)



            else:
                data = str(len(data))
                conn.sendall(data.encode())                                  # отправляет данные

print(keys)








