# Example 4
# Написать декоратор к 2-м любым функциям,который бы считал и выводил время их выполнения

from datetime import datetime
import time

def timer(funk):                                       #функция декоратор подсчета времени
  def dek(*args,**kwargs):
       time = datetime.now()
       funk(*args,**kwargs)
       time2=datetime.now()
       print("Время работы функции", (time2-time))
  return dek

@timer
def foo(a):                                            # функция 1
   for i in range(a):
       if i<5:
           print(i*2)
           time.sleep(1)

foo(100)

@timer
def bar(a):                                            # функция 2
    reversed_string = a[::-1]
    print(reversed_string,sep="\n")
    time.sleep(3)
bar("Hello, world!")