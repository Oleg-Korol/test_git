name = 'vova'

assert len(name) == 4
# print(name.__doc__)

print(name.lower())
print(name.upper())

print('hello name {}'.format(name))
print(f'hello name {name}')
print(f"hello name {name}")
print(f"hello name '{name}'")
print(f'hello name "{name}"')

assert name.isalpha()
assert not name.isdigit()

# арифметическе операторы
assert not (1 != 1)

assert 10 % 2 == 0
assert 2**3 == 8

assert 12 // 5 == 2


#  операторы сравнения
# ==
# !=
# <>
# >
# <
# >=
# <=

assert 2**3 + 1 == 9
assert 2**(3 + 1) == 9

