# Example 2
# Дан список чисел
# Вернуть список где при помощи функции map() каждое число переведено в строку.
# В качестве функции в map()  использовать lambda


spisok=[1,2,3,4,5,6,7,8,9]
string=list(map(lambda x:str(x), spisok))
assert string[0]=='1'
