# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 5, Задание 3
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
#

path = "files/"
input_file = "text_3.txt"

with open(path+input_file, "r", encoding="utf-8") as file_descriptor:
    r_str = file_descriptor.readlines()

salary = []
summa = 0
for i in r_str:
    salary = i.rstrip().split(" ")
    if float(salary[1]) < 20000:
        print(f"{salary[0]} -> {salary[1]}")
    summa += float(salary[1])

print(f"Средняя заработная плата всех сотрудников компании: {summa / len(r_str)}")
