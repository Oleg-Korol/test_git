# Example 1.
# Есть список, содержащий кортежи [(1, 2), (3, 4), (5, 6)]
# Используя list comprehension получить список, содержащий сумму элементов кортежа


spisok=[(1, 2), (3, 4), (5, 6)]
spisok_sum=sum([i for kortej in spisok for i in kortej])
assert spisok_sum==sum(range(7))