# Example 1.
# Сделать калькулятор
from hw_03_09 import Big_number_error

def calculator():
 while True:
    print("Выберите операцию:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")
    action=input()
    if action not in ('+', '-', '*', '/', "q"):
        raise ValueError                                                    # возбуждаем ValueError
        break
    if action=="q":
      print("Выход из программы")
      break
    if action in ('+', '-', '*', '/'):
        x = float(input("x = "))
        y = float(input("y = "))
        if len(str(x)) > 10 and len(str(y)):                                # возбуждаем свое исключение из задания №3
            raise Big_number_error
            break
        if action == '+':
            return x+y
        elif action == '-':
            return x - y
        elif action == '*':
            return x*y
        elif action == '/':                            # оставил в таком виде, чтобы вызвать ошибку при делении на ноль
                return x/y

