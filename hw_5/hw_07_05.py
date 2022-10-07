# Ex. 7
# Написать декоратор, который кэширует результат выполнения ф-и и
# при повторном вызове с такими же аргументами выдает результат из кэша



bank={}
def cash_multiply(funk):
    def wrapper(*args):
        global bank
        if args[0] in bank:
            return bank[args[0]]
        value=funk(*args)
        bank[args[0]]=value
        print(bank)
        return value
    return wrapper

@cash_multiply
def multiply(n):
    if n in bank:
        return bank[n]
    return n*1000
print([multiply(n) for n in range(10)])
assert bank[1]==1000
assert bank[5]==5000
