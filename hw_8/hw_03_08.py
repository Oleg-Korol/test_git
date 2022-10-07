# Ex.3
# Добавить в TechnicalStaff статичный метод get_info(employee), получающий данные от работника и если работник из того же
# департамента - выдавать приветствие.


from hw_01_08 import Employee

Employee.departament = None


class TechnicalStaff(Employee):

     def change_department(value):
        TechnicalStaff.departament = value

     @staticmethod                                                  # Задание 3
     def get_info(employee):
         if employee.departament ==TechnicalStaff.departament:
             return print("Hello, friend")
         else: return print("Different departments")



assert TechnicalStaff.departament == None
TechnicalStaff.change_department("Biotechnologies")
assert TechnicalStaff.departament == "Biotechnologies"


b=TechnicalStaff("Vladislav","Petrov",30,"technologist")
b.departament="Biotechnologies"
TechnicalStaff.get_info(b)


c=TechnicalStaff("Maks","Sidorov",35,"Security")
c.departament="Department_of_Security"
TechnicalStaff.get_info(c)



# assert c.get_info()!="Hello, friend!"
# print(b.__dict__)