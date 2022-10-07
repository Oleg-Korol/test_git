# Example 2.
# Дан словарь. Создать новый словарь, поменяв местами ключ и значение

shkala_tverdosti={"Тальк":"1",
              "Гипс":"2",
              "Кальцит":"3",
              "Флюарит":"4",
              "Апатит":"5"}
zamena={k:v for v,k in shkala_tverdosti.items()}
assert zamena["1"]=="Тальк"
assert zamena["5"]=="Апатит"
