# Прочитать сохранённый json файл и записать данные на диск в csv-файл, первой
# строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.

import json
with open('baza_people.json',"r") as json_file:
    baza = json.load(json_file)
    print(baza)
phone=["12322343","34343434","84848488","23223232","93993993"]

import csv

name = ['Id', 'name', 'Age','Phone']

with open("csvfile.csv", 'w') as f:
    wr = csv.DictWriter(f,delimiter=";", fieldnames = name)
    wr.writeheader()
    wr.writerows(baza)
    wr = csv.writer(f)

