# Ex.3
# Используя библиотеку requests, отправить get-запрос ресурсам
# - локальному серверу с ex_01_serv.py
# - ресурсам в internet, на свой выбор (yandex, google)
#


import requests

response= requests.get('http://localhost:8000')
assert response.status_code == 200


r = requests.get('http://google.com')
assert r.status_code == 200

