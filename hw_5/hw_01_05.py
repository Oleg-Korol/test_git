# Example.1
# Написать лямбда функцию определяющую чётное/нечётное.
# Функция принимает параметр(число)  и если чётное то выдаёт слово “чётное”, если нет - то “нечётное”


even_or_odd=(lambda a : print("четное") if a%2==0 else print("нечетное"))(int(input("Введите число:")))

