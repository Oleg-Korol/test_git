# Ex.2
# Добавить в Employee атрибут класса department = None
# Унаследовать от Employee класс TechnicalStaff в котором реализовать метод класса change_department, позволяющий менять департамент
# Добавить в свойство info данные о департаменте


from hw_01_08 import Employee

Employee.departament = None


class TechnicalStaff(Employee):

     def change_department(self,value):
        TechnicalStaff.departament = value


assert TechnicalStaff.departament == None
b=TechnicalStaff("Vladislav","Petrov",30,"technologist")
b.change_department("Biotechnologies")
assert TechnicalStaff.departament == "Biotechnologies"

