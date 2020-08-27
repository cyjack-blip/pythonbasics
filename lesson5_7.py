# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 5, Задание 7
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
#

import json

path = "files/"
input_file = "text_7.txt"
output_file = "text_7.json"

with open(path+input_file, "r", encoding="utf-8") as file_descriptor:
    r_str = file_descriptor.readlines()

firm_data = []
for a in r_str:
    firm_data.append(a.strip().split(" "))

i = 0
n = 0
average = 0
for a in firm_data:
    dohod = int(a[2]) - int(a[3])
    if dohod >= 0:
        i += dohod
        n += 1
    average = i / n

firms_profit = {}

for a in firm_data:
    firms_profit[a[0]] = int(a[2]) - int(a[3])

result = [firms_profit, {"average_profit": average}]

with open(path+output_file, "w", encoding="utf-8") as file_descriptor:
    json.dump(result, file_descriptor, sort_keys=True, indent=4, ensure_ascii=False)
