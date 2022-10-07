# 1.Декодировать в строку байтовое значение b'r\xc3\xa9sum\xc3\xa9'
# 2.Результат преобразовать в байтовый вид в кодировке "Latin1"
# 3Результат снова декодировать в строку
# 4.Результаты преобразования выводить на экран

my_str_bytes= b'r\xc3\xa9sum\xc3\xa9'
my_str=my_str_bytes.decode('utf-8')
assert isinstance(my_str, str)
print(my_str)
my_str_latin1=my_str.encode('latin1')
assert isinstance(my_str_latin1, bytes)
print(my_str_latin1)
my_str2=my_str_latin1.decode('latin1')
assert isinstance(my_str2, str)
print(my_str2)