"""
Создайте класс Calculator который поддерживает:
- сложение двух чисел
- вычисление разницы между двумя числами
- умножение двух чисел
- деление одного числа на другое
Примеры вызовов и возвратов из функций:
calculator = Calculator()
calculator.add(10, 5) ➞ 15
calculator.subtract(10, 5) ➞ 5
calculator.multiply(10, 5) ➞ 50
calculator.divide(10, 5) ➞ 2
"""


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a,  b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        try:
            return a // b
        except ZeroDivisionError as ex:
            return f"Ошибка: {ex}"


calculator = Calculator()
print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
