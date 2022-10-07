 # Ex. 8
# Дан список чисел. Найти сумму чисел, кратных 3 и 5.
# Реализовать через filter
# Написать тесты.

my_list = [x+1 for x in range(100)]
print("Исходный список",my_list)

filtered3 = list(filter(lambda x:x%3==0 and x%5 == 0 , my_list))
assert filtered3[0]==15
sum_final=sum(filtered3)
print("Cумма чисел кратных двум значениям(3,5):",sum_final)

