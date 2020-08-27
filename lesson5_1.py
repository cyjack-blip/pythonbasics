# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 5, Задание 1
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
#


path = "files/"
output_file = "output1.txt"

print("Вводит строки, пока не надоест. Когда надоест, введите пустую строку.")

file_descriptor = open(path+output_file, "w", encoding="utf-8")
while True:
    u_string = input(": ")
    if u_string == "":
        break
    else:
        print(u_string, file=file_descriptor)

file_descriptor.close()
