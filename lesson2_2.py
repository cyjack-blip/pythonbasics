# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 2, Задание 2
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#

#
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()
#

uInput = input("Введите список значений, разделенных запятыми: ")
# разделили строку ввода и вырезали пробелы
uList = [i.lstrip() for i in uInput.split(',')]

print("Начальный список:\n", uList)

# если нечетное количество элементов в списке, то вытолкнем лишний элемент
last = None
if len(uList) % 2:
    last = uList.pop()

# поменяем местами элементы
n = 0
for i in uList:
    if (n % 2) == 0:
        uList.insert(n, uList.pop(n+1))
    n += 1

# добавим последний элемент, если его рантше выталкивали
if last:
    uList.append(last)

print("Конечный список:\n", uList)
