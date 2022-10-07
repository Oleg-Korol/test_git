# Ex. 3
# Добавить в ex.2 бесконечный цикл.
# Выход из цикла сделать через ввод симолов "Q", "q"


def privetstvie(i):
    name = input("Введите свое имя:")  # ввод имени
    while name.isdigit()==True:                         #  Бесконечный цикл
        print("Вы ввели имя состоящее из цифр")         #
        b=input()                                       #
        if b=="q" or b=="Q":                            # Обьявляем переменные для выхода из цикла
            break                                       # Выход из цикла While
    if not i.isdigit():                                 # проверка на число
        print("Ошибка,повторите ввод")
        return 0
    if int(i) <= 0:                                      # фильтрация согласно заданным условиям
        print("Ошибка,повторите ввод")
        return 0
    if 0 < int(i) < 10:
        print(f'Привет, малыш {name}')
        return 0
    if 10 <= int(i) <= 18:
        print(f"Как дела {name}?")
        return 0
    if 18 < int(i) <= 120:
        print(f"Что желаете {name}?")
        return 0
    else:
        print(f"{name} вы лжете - столько не живут")


privetstvie(input("Введите свой возраст:"))                    #Ввод возраста