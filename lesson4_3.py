# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 4, Задание 3
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
#

# 240 входит в пределы?
my_list = [a for a in range(20, 241) if a % 20 == 0 or a % 21 == 0]

print(my_list)