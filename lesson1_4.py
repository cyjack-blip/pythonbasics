# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 1, Задание 4
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#

#
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#

num = i = int(input("Введите целое положительное число: "))

maxDigit = num % 10

while (i % 10) > 0:
    if maxDigit < i % 10:
        maxDigit = i % 10
    i = i // 10

print(f"В числе {num} максимльное значение разряда {maxDigit}")
