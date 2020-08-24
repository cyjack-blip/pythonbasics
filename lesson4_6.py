# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 4, Задание 6
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
#

from itertools import count, cycle


def make_pi(precision):
    """итератор выдает знаки pi на precision шагов, целая 3 входит в диапазон"""
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(precision * 4):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


def iterator(start, steps):
    """итератор  выдает целые числа от start на steps раз"""
    for el in count(start):
        if el < start + steps:
            yield el
        else:
            return


def cycle_iterator(pi_precision, steps):
    """циклический итератор выдает значения steps раз, в качестве списка используется значения числа pi на n знаков"""
    my_list = []
    # инициализируем список циклического итератора знаками числа pi на pi_precision знаков
    for i in make_pi(pi_precision):
        my_list.append(str(i))
    for el in cycle(my_list):
        if steps <= 0:
            return
        else:
            steps -= 1
            yield el


iterator_list = []
cycle_iterator_list = []

start = 10  # от какого числа генерируем список в простом генераторе
steps = 30  # количество итераций в обоих итератотрах
pi_precision = 10  # сколько знаков числа pi сгенерировать во втором итераторе

for i in iterator(start, steps):
    iterator_list.append(i)

for i in cycle_iterator(pi_precision, steps):
    cycle_iterator_list.append(i)

print(f"Простой итератор.\nГенерация {steps} чисел, начиная с {start}:\n{iterator_list}\n")
print(f"Циклический итератор по предварительно заданному списку.\n\
Генерация {steps} чисел из списка {pi_precision} знаков числа pi\n{cycle_iterator_list}")