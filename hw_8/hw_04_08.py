# Ex.4
# Есть класс Account.
# Конструктор принимает person_id (уникальный), currency (реализовать через enum) и amount (кол-во денег на счету).
# Person_id можно релазиовать через uuid4.
# Реализовать свойство amount, которое при попытке записать в значение сумму <0 - выдает ошибку (либо предупреждение и не меняет значение)
# См. getter/setter



class Account:
    def __init__(self,person_id,ammount:int):
        self.person_id=person_id
        self.__ammount= ammount
        self.currency = "RUB"


    @property
    def ammount(self):
         return print(self.__ammount)

    @ammount.setter  # измненение пароля
    def ammount(self,value):
        if  isinstance(value,(int,float)) and value > 0:
            self.__ammount=value
        else:
            raise ValueError("Некорректная сумма")

a=Account(121223334,100)
print(a.__dict__)
a.ammount
a.ammount=100000
a.ammount
a.ammount=-2000

