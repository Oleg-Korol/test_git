# Example_4
# Таблицу Location
# - street_address
# - postal_code
# - city
# - country_id
#
# Таблицу Countries
# - name
#
# Реализовать функцию, возвращающую список городов в алфавитном порядке. Учесть дубликаты
#

import sqlite3
from sqlite3 import Error
from hw_12 import create_connection,execute_query,execute_read_query

connection = create_connection()

#создаем таблицу
create_users =("""CREATE TABLE IF NOT EXISTS location(
               street_address VARCHAR(30),
               postal_code INTEGER PRIMARY KEY,
               city VARCHAR(15),
               country_id VARCHAR(15))""")

execute_query(connection, create_users)

create_users_table2 =("""CREATE TABLE IF NOT EXISTS country(
                 name VARCHAR(20) PRIMARY KEY)
                 """)
execute_query(connection, create_users_table2)



#заполняем таблицу
create_users =("""INSERT INTO location(street_address,postal_code,city,country_id)
        VALUES('Pushkinckaya',221161,'Minsk','Belarus'),
              ('Kirava',224411,'Brest','Belarus'),
              ('Lenina',221671,'Gomel','Belarus'),
              ('Maiskaya',221681,'Gomel','Belarus'),
              ('Serova',221141,'Minsk','Belarus'),
              ('Esenina',221111,'Grodno','Belarus')""")

create_users2 =("""INSERT INTO country(name)
              VALUES('Belarus'),
              ('Russia'),
              ('USA'),
              ('Chine'); """)
execute_query(connection,create_users)
execute_query(connection,create_users2)

 #выводим таблицы
select_users = "SELECT * from location"
users = execute_read_query(connection, select_users)
for user in users:
     print(user)

print("\n")


select_users = "SELECT * from country"
users = execute_read_query(connection, select_users)
for user in users:
     print(user)




# выводим отсортированный список городов
curs = connection.cursor()
curs.execute("SELECT DISTINCT city  FROM location ORDER BY city ")
print((curs.fetchall()))

