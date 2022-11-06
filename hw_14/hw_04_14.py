# Ex.4
# Разобраться, как работать с ресурсом http://numbersapi.com/
# Отправить get /post запросы, используя requests.
# Создать БД numbersapi. Продумать структуру таблиц для сохранения запросов/ответов.


#Суть идеи:
# Программа запрашивает на ввод год и месяц.
# Определяет число дней в месяце.
# Исходя из полученных данных (месяца и чисел) делает запрос на numbersapi.com и получает события происходящие в заданном месяце
# Если полученный год события совпадает с введенным нами (увеличил период +-10 лет чтобы ускорить поиск) то данное событие заносится в таблицу
# Ограничил поиск найденым значением или 10 циклами

import requests
import sqlite3
import calendar
from Func_table import  create_connection,execute_query,execute_read_query


connection = create_connection()
create_users_table =("""CREATE TABLE IF NOT EXISTS history_date(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date INTEGER(2),
                 moth VARHAR(10),
                 year VARHCAR(4),
                 event VARCHAR(200) );""")
execute_query(connection, create_users_table)


def sql_insert(con, val):  # добавляем данные в таблицу
   curs = con.cursor()
   curs.execute("""INSERT INTO history_date(date,moth,year,event) VALUES(?,?,?,?)""", val)
   con.commit()


y = int(input('Введите год: '))
m = int(input('Введите месяц: '))
d=calendar.monthrange(y, m)[1]
print(f'Количество дней в месяце:{d}')
period=[x for x in range(y-10,y+10)]

Flag=False
count=1

while Flag!=True and count<=10:
   print(f'Поиск... цикл номер {count} из 10')
   count+=1

   for i in range(1,d+1):
      response= requests.get(f'http://numbersapi.com/{m}/{i}/')
      assert response.status_code == 200
      evant = response.text
      for j in period:
         if str(j) in response.text:
            Flag=True
            evant = response.text
            sql_insert(connection,(i,m,j,evant))



#выводим таблицу
select_users = "SELECT * from history_date"
users = execute_read_query(connection, select_users)
for user in users:
       print(user)