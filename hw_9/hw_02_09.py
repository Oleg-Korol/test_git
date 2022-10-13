# Example 2.
# Обернуть калькулятор в try/except

from hw_01_09 import calculator
from hw_03_09 import Big_number_error
try:
    print(calculator())
except ValueError:
    print("Введен не существующий оператор")
except ZeroDivisionError:
    print("На ноль делить нельзя")
except Big_number_error:
    print("Большое число.Стоит ограничение в 10 симвалов")
