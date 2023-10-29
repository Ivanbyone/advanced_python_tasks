"""
Создать класс Name, который принимает имя и фамилию в качестве аргументов при конструировании.
Класс должен поддерживать атрибуты:
first_name, возвращающий имя
last_name, возвращающий фамилию
full_name, возвращающий имя и фамилию
initials, возвращающий инициалы
Класс должен приводить переданные имя и фамилию в форму при которой имя и фамилия начинаются с заглавной буквы,
а все остальные буквы в нижнем регистре (поскольку вызывающий код может передавать такие строки как "JOHN", 'jOHN',
'sMiTh' и т.д.)
Примеры вызовов:
a1 = Name('john', 'SMITH')
a1.first_name ➞ 'John'
a1.last_name ➞ 'Smith'
a1.full_name ➞ 'John Smith'
a1.initials ➞ 'J.S'
"""


class Name:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = self.first_name + ' ' + self.last_name
        self.initials = self.first_name[0] + '.' + self.last_name[0]


a1 = Name('john', 'SMITH')
print(a1.first_name)
print(a1.last_name)
print(a1.full_name)
print(a1.initials)
