# Ex. 4
# Ф-я принимает список целых чисел и возвращает минимальное число, максимальное число, среднее-арифметическое.


from ast import literal_eval
def numbers (n:int):
    print("max:",max(n),"\n"
        "min:",min(n),"\n"
        "sr.arf:",sum(n)/len(n))
    assert max(n)>min(n)
    return max(n), min(n), sum(n) / len(n)
numbers(literal_eval(input('Введите список состоящий из целых чисел: ')))