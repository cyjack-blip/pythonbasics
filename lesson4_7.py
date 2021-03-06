# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 4, Задание 7
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
#   а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
#

def fact(n):
    x = 1
    my_list = []
    for i in range(1, n+1):
        x *= i
        my_list.append(i)
        yield x, my_list


n = 5

for i, el in enumerate(fact(n)):
    print(f"{i+1}! =", " * ".join(map(str, el[1])), "=", el[0])
