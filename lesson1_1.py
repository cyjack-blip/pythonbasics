# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 1, Задание 1
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#

#
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
#

years2add = 5
name = input("Как вас зовут?: ")
age = int(input("Сколько вам лет?: "))

print("Привет, "+name)
print("Через 5 лет вам будет "+str(age+years2add))
