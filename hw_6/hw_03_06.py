# Создать словарь ключ-id, значение кортеж - (имя , возраст)
# Записать данный словарь на диск в json-фаил
import json

identification=[{"Id":'227177', "name":"Mark","Age":"35"},
                {"Id":'236789', "name":"Anna","Age":"23"},
                {"Id":'899345', "name":"Maria","Age":"27"},
                {"Id":'455327', "name":"Alex","Age":"31"},
                {"Id":'333676', "name":"Dima","Age":"42"},
                {"Id":'992387', "name":"Viktoria","Age":"20"}

                 ]
with open("baza_people.json","w") as write_file:
    json.dump(identification, write_file)
