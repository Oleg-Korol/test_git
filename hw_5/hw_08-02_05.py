# Ex. 8
# Дан список чисел. Найти сумму чисел, кратных 3 и 5.
# Реализовать через reduce
# Написать тесты.
from functools import reduce

def reduse_funk(my_list):
    a=reduce(lambda a,x:a+x if x % 3 == 0 and x % 5 == 0 else a+0 ,my_list,0)
    return a
reduse_funk([x+1 for x in range(100)])
assert reduse_funk([0,15,30,7,4,2])==45