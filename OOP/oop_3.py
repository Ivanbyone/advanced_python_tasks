"""
Создать класс Employee, который принимает имя, фамилию и зарплату в качестве аргументов при конструировании.
Класс должен поддерживать:
- атрибут first_name, возвращающий имя
- атрибут last_name, возвращающий фамилию
- атрибут salary, возвращающий зарплату
функцию from_string, которая принимает имя, фамилию и зарплату в формате 'first_name-last_name-salary',
парсит строку и возвращает экземпляр Employee
Примеры:
emp1 = Employee('Mary', 'Sue', 60000)
emp2 = Employee.from_string('John-Smith-55000')
emp1.first_name ➞ 'Mary'
emp1.salary ➞ 60000
emp2.first_name ➞ 'John'
emp2.salary ➞ 55000
"""


class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, str1):
        first_name, last_name, salary = str1.split('-')
        return cls(first_name, last_name, int(salary))


emp1 = Employee('Mary', 'Sue', 60000)
emp2 = Employee.from_string('John-Smith-55000')
print(emp1.first_name)
print(emp1.salary)
print(emp2.first_name)
print(emp2.salary)
