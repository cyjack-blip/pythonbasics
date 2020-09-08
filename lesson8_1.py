# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 8, Задание 1
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
#
from datetime import datetime


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def convert(cls, day_month_year):
        my_date = day_month_year.split("-")
        return int(my_date[0].strip()), int(my_date[1].strip()), int(my_date[2].strip())  # day, month, year

    @staticmethod
    def validate(day, month, year):
        try:
            datetime(year, month, day)
        except ValueError as err:
            return f'Ошибка: {err}'
        else:
            return f'Корректная дата'

    def __str__(self):
        return f'Текущая дата {self.convert(self.day_month_year)}'


today = Date('12 - 8 - 2019')

print(today)
print(Date.validate(11, 11, 2022))
print(today.validate(11, 13, 2011))
print(Date.convert('11 - 11 - 2011'))
print(today.convert('11 - 11 - 2020'))
print(Date.validate(1, 11, 2000))
