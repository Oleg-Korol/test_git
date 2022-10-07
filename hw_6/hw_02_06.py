# 1.Ввести 4 строки  и сохранить их в 4 переменные
# 2.Создать фаил, внести в него первые 2 строки, закрыть фаил
# 3.Открыть и дозаписать оставшиеся 2 строки
# 4.В итоговом файле 4 строки, каждая начинается с новой строки

m="Hellow, Minsk!"
g="Hellow, Grodno!"
b="Hellow, Brest!"
v="Hellow, Vitebsk!"

f=open("hello_sity.txt","w")
f.write(m+ '\n')
f.write(g+ '\n')
f.close()
f=open("hello_sity.txt","a")
f.write(b+ '\n'+v)