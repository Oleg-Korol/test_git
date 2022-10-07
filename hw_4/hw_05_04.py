# Написать ф-ю, которая выводит сегодн дату, текущее время и приветствие.

def hello_data_time():
    import datetime
    a=datetime.datetime.now()
    print(f'Привет! Сегодн. дата и текущее время: {a}')
hello_data_time()