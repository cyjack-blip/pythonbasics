# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 3, Задание 2
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
#

def user_info(**kwargs):
    output_string = ""
    for key, value in kwargs.items():
        output_string += "{}: {} / ".format(key, value)
    print(output_string.lstrip())


user_info(firstname="Иван", lastname="Иванов", birthyear=1990, city="Москва", email="ivan.ivanov@mail.ru", phone="1234567890")
user_info(firstname="Андрей", lastname="Краснов", birthyear=1975, phone="1234567890")
user_info(firstname="Татьяна", lastname="Петрова", birthyear=1992, city="Сочи", phone="1234567890")
