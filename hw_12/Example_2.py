# Example 2
# Таблицу работников Employees
# - first_name
# - last_name
# - email
# - phone_number
# - hire_date
# - job_id
# - manager_id
# - department_id
#
#
# Реализовать функцию, возвращающую количество руководителей

import sqlite3
from sqlite3 import Error
from hw_12 import create_connection,execute_query,execute_read_query

connection = create_connection()

#создаем таблицу
create_users_table =("""CREATE TABLE IF NOT EXISTS Employees(
                 first_name  varchar(10),
                 last_name   varchar(15),
                 email       varchar(15),
                 phone_number varchar(15),
                 hire_date   varchar(10), 
                 job_id        varchar(15),
                 manager_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                 department_id  int );""")
execute_query(connection, create_users_table)

#заполняем таблицу
create_users =("""INSERT INTO Employees(first_name,last_name,email,phone_number,hire_date,job_id ,department_id) 
                VALUES('Ivan','Ivanov', 'qwqw@.com','232-43-42','01.02.2019',5,"Bank"),
                ('Mark','Petrov', 'qcxx@.com','252-53-62','06.06.2019',7,"Bank"),
                ('Alex','Sidorov', 'dfdffdw@.com','255-43-33','11.07.2022',9,"Bank")""")
execute_query(connection,create_users)

# выводим таблицу
select_users = "SELECT * from Employees"
users = execute_read_query(connection, select_users)
for user in users:
     print(user)


# выводим общее кол-во руководителей
print("Количество менеджеров",end=":")
curs = connection.cursor()
curs.execute("SELECT * FROM Employees")
print(len(curs.fetchall()))