Example 3

# При помощи функции filter() из котрежа слов отфильтровать только те,
# которые являются полиндромами (читаются одинаково в обе стороны)


kortej = ("казак", "мед", "человек", "потоп", "дед", "осень")
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string
a = tuple(filter(lambda x:x in x==''.join(reversed(x)),kortej))
print(a)
assert "казак" in a
assert "мед" not in a
