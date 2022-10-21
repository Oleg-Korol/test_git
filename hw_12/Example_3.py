# Example 3
#
# Таблицу Jobs
# - title
# - min_salary
# - max_salary
#
# еализовать функцию, возвращающую среднее значение зарплаты

import sqlite3
from sqlite3 import Error
from hw_12 import create_connection,execute_query,execute_read_query

connection = create_connection()

#создаем таблицу
create_users_table =("""CREATE TABLE IF NOT EXISTS jobs(
                 title str PRIMARY KEY,
                 min_salary int,
                 max_salary int );""")
execute_query(connection, create_users_table)


#заполняем таблицу
create_users =("""INSERT INTO jobs(title,min_salary,max_salary) 
              VALUES('Belarusneft',800,3000),
              ('Belaz',1000,5000),
              ('Keramin',600,2000),
              ('Volat',1000,3000),
              ('Azot',1000,3500)""")
execute_query(connection,create_users)

# выводим таблицу
select_users = "SELECT * from jobs"
users = execute_read_query(connection, select_users)
for user in users:
     print(user)

# рассчитываем среднюю зп
curs = connection.cursor()
curs.execute('SELECT AVG(min_salary) FROM jobs')
b=curs.fetchone()
curs.execute('SELECT AVG(max_salary) FROM jobs')
c=curs.fetchone()
print("Cредняя минимальная:",b,"Cредняя максимальная:",c)


