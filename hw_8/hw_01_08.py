# Ex.1
# Создать класс Employee.
# Конструктор принимает first_name, last_name, age, profession.
# Person должен иметь свойство onboarding_time (выставляется по-умолчанию при создании объекта)
# Person должен иметь свойство info, возвращающее словарь
# {
#     "fullname": полное_имя работника,
#     "age": возраст работника,
#     "working_time": количество времени, которое прошло с момента onboarding_time
# }
import datetime
import time


class Employee:



    def __init__(self,first_name:str,last_name:str,age:int,profession:str):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.professional=profession
        self._time=datetime.datetime.now()


    @property
    def onboarding_time(self):
        return self._time


    @property
    def info(self):
        time_delta=datetime.datetime.now()-self._time
        baza= {'fullname':str(self.first_name+" "+self.last_name),'age':self.age,'working_time':time_delta}

        return baza


a=Employee("Alex","Ivanov",25,"engineer")
time.sleep(3)
print(a.info)


