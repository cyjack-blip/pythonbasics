# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 5, Задание 4
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#

vocabulary = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре", 5: "Пять", 6: "Шесть", 7: "Семь", 8: "Восемь", 9: "Девять"}

path = "files/"
input_file = "text_4.txt"
output_file = "output4.txt"

r_list = new_list = []

with open(path+input_file, "r", encoding="utf-8") as file_descriptor:
    r_str = file_descriptor.readlines()

with open(path+output_file, "w", encoding="utf-8") as file_descriptor:
    for i in r_str:
        r_list = i.rstrip().split(" - ")
        new_list.append(f"{vocabulary.get(int(r_list[1]))} - {r_list[1]}")
    file_descriptor.writelines("%s\n" % line if line != new_list[len(new_list)-1] else "%s" % line for line in new_list)
