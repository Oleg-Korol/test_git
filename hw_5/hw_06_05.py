
# Ex. 6
# Написать реккурсивную ф-ю, вычисляющую N-е число ряда Фибоначчи.
# Продумать проверки + написать тесты.


def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib (n-1) + fib (n-2)
assert fib(2)==1
assert fib(10)==55