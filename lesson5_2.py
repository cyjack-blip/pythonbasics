# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 5, Задание 2
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
#

# file from previous task
path = "files/"
input_file = "output1.txt"

i = 0
words = []
with open(path+input_file, "r", encoding="utf-8") as file_descriptor:
    r_str = file_descriptor.readlines()

print(f"Коичество строк: {len(r_str)}")
for i in r_str:
    words.append(len(i.split(" ")))

print(f"Количество слов по строкакм: {words}")
