# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 5, Задание 5
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#

from random import randint

path = "files/"
output_file = "output5.txt"

rand_range = 50  # интервал генерации случайных чисел
rand_num = 20  # количество чисел для генерации

# сгенерировали список случайных чисел
num_list = [randint(1, rand_range) for _ in range(rand_num)]

# записали числа в файл
with open(path+output_file, "w", encoding="utf-8") as file_descriptor:
    file_descriptor.writelines("%s " % line for line in num_list )

# прочитали из файла
with open(path+output_file, "r", encoding="utf-8") as file_descriptor:
    r_str = file_descriptor.read()

summa = 0
r_str = r_str.split()
for i in r_str:
    summa += float(i)

print(summa)
