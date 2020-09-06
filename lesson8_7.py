# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 8, Задание 7
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров.
# Проверьте корректность полученного результата.
#

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        # (a + bi) + (c + di) = (a + c) + (b + d)i
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        # (a + bi) * (c + di) = (ac - bd) + (bc + ad)i
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
z_3 = ComplexNumber(2, 3)

print(z_1)
print(z_1 + z_2 + z_3)
print(z_1 * z_2 * z_3)
