# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 7, Задание 3
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
#
from abc import ABC, abstractmethod


class Textil:
    """название, размемр (V и H), набор параметров"""
    consumption = [[6.5, 0.3], [2, 0.3]]

    def __init__(self, title, metrika, consumption_type):
        self.title = title
        self.size = metrika
        self.consumption_formula = [self.consumption[consumption_type][0], self.consumption[consumption_type][1]]

    @abstractmethod
    def get_cloth_square(self):
        pass


class Clothes(Textil):
    def __init__(self, width, height, consumption_type):
        super().__init__(width, height, consumption_type)

    @property
    def get_cloth_square(self):
        return self.size / self.consumption_formula[0] + self.consumption_formula[1]

    def __add__(self, other):
        return self.get_cloth_square + other.get_cloth_square


coat = Clothes("пальто", 4, 0)
jacket = Clothes("костюм", 10, 1)

print(f"Расход ткани на {coat.title}: {coat.get_cloth_square:.4f}")
print(f"Расход ткани на {jacket.title}: {jacket.get_cloth_square:.4f}")

print(f"Общий расход ткакние: {(coat + jacket):.4f}")
