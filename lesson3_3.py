# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 3, Задание 3
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
#

def my_func(num1, num2, num3):
    mlist = [float(num1), float(num2), float(num3)]
    mlist.remove(min(mlist))
    return sum(mlist)


uNum = input("Введите три числа, разделенных пробелом: ")
uNumSplit = uNum.split()

try:
    for i in uNumSplit:
        float(i)
    print(my_func(uNumSplit[0], uNumSplit[1], uNumSplit[2]))
except ValueError:
    print("Ошибка, одно из значений не число")
except IndexError:
    print("Ошибка, введено слишком мало чисел")
