# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 5, Задание 6
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика:   100(л)   50(пр)   20(лаб).
# Физика:   30(л)   —   10(лаб)
# Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#

import re

path = "files/"
input_file = "text_6.txt"

# прочитали файл построчно
with open(path+input_file, "r", encoding="utf-8") as file_descriptor:
    r_str = file_descriptor.readlines()

subject_tmp_list = []
subject_list = {}
hours_list = []
for a in r_str:
    tmp1 = a.split(":")
    tmp2 = tmp1[1].strip().split(" ")  # ['-', '30(пр)', '-']
    subject_tmp_list.append(tmp1[0])  # делаем список предметов
    hours = 0
    num = []
    for n in tmp2:  # переберам список с часами, чтобы вытащить цифры
        num = re.findall(r'\d+', n)
        num = [int(k) for k in num]
        if len(num) > 0:
            hours += num[0]
    hours_list.append(hours)  # создаем список с суммой часов

# сделаем итотговый словарик из двух списков
for n, k in enumerate(subject_tmp_list):
    subject_list[k] = hours_list[n]

print(subject_list)


