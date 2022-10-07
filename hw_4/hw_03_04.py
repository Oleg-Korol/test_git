# Ex. 3
# На вход функции подается натуральное число n.
# Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 1 до n,
# а затем выводит его элементы построчно, то есть каждый на отдельной строке.



def kvadrat_numbers(a):
    spisok_kvadrat_numbers=[(x+1)*(x+1) for x in range(a)]
    assert spisok_kvadrat_numbers[-1]==a*a
    [print (i) for i in spisok_kvadrat_numbers]
kvadrat_numbers(10)