# Example 1
# Создать таблицу департаментов.
# Departments содержит
# - name
# - manager_id
# - location_id
#
# Реализовать механизм первичных ключей. Продумать, какие типы будут присвоены полям
# Реализовать функционал, позволяющий вставлять, обновлять, удалять записи в таблицах.
#
#
# Реализовать функцию, возвращающую количество работников в отделе

import sqlite3
from sqlite3 import Error
from hw_12 import create_connection,execute_query,execute_read_query

connection = create_connection()
#создаем таблицу
create_users_table =("""CREATE TABLE IF NOT EXISTS departaments(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name str,
                 manager_id ,
                 location_id str );""")
execute_query(connection, create_users_table)

#заполняем таблицу
create_users =("""INSERT INTO departaments(name,manager_id,location_id) 
               VALUES('IT', 5, 'Minsk'),
               ('Math', 6, 'Vitebsk'),
               ('Chemical', 7, 'Grodno'),
               ('IT', 7, 'Gomel'),
               ("English",3,"Minsk")
               """)
execute_query(connection,create_users)

#добавляем данные в таблицу
def sql_insert(conection,val):
    curs = conection.cursor()
    curs.execute("""INSERT INTO departaments(name,manager_id,location_id) VALUES(?,?,?)""", val)
    conection.commit()


date=(('Music', 5, 'Minsk'),('language', 6, 'Vitebsk'),('biology', 7, 'Grodno'),('physics', 7, 'Gomel'))
for val in date:
    sql_insert(connection,val)


# выводим таблицу
select_users = "SELECT * from departaments"
users = execute_read_query(connection, select_users)
for user in users:
     print(user)

#редактируем таблицу(в департаменте Сhamical меняем кол-во человек с 7 на 10)
update_sql=("""UPDATE departaments SET manager_id = 10 where name = 'Chemical' """)
execute_query(connection,update_sql)


# удаляем строку N5
delete_comment = "DELETE from departaments WHERE id = 5"
execute_query(connection, delete_comment)

# выводим таблицу
users = execute_read_query(connection, select_users)
for user in users:
    print(user)

#выводим кол-во сотрудников в IT отделе
def worker(connection):
    curs = connection.cursor()
    curs.execute("""SELECT SUM(manager_id)  FROM departaments WHERE name='IT'""")
    result = curs.fetchone()
    return result

print("Количество сотрудников в отделе 'IT'=",*worker(connection))
