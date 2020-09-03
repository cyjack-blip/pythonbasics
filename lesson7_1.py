# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 7, Задание 1
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
#


class Matrix:
    def __init__(self, m_list):
        self.m_list = m_list

    def __add__(self, other):
        tmp_matrix = []
        tmp_vector = []
        for n in range(len(self.m_list)):
            tmp_vector.clear()
            for m in range(len(self.m_list[n])):
                tmp_vector.append(self.m_list[n][m] + other.item(n, m))
            tmp_matrix.append(tmp_vector)
        return Matrix(tmp_matrix)

    def item(self, n, m):
        return self.m_list[n][m]

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.m_list]))


a = Matrix([[1, 2, 3, 4], [1, 2, 3, 4]])
b = Matrix([[1, 1, 1, 1], [1, 1, 1, 1]])

print(a + b)
