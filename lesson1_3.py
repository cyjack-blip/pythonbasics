# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 1, Задание 3
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#

#
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#

# float or string unsafe
a = int(input("Введите число: "))

# проверка на отрицательное число
if a < 0:
    a *= -1

b = int(str(a)+str(a))
c = int(str(a)+str(b))

result = a + b + c

print(f"{a} + {b} + {c} = {result}")
