# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 6, Задание 2
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
#

class Road:
    """класс дорога(длинна, ширина)"""
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square(self):
        """метод площадь = длинна * ширина"""
        return self._length * self._width


class MassCount(Road):
    """атрибут: масса 1 кв м дороги толщиной 1 см"""
    __mass_per_meter = 25

    def __init__(self, _length, _width, thickness):
        self._thickness = thickness
        super().__init__(_length, _width)

    def mass(self):
        """метод масса дороги = площадь дороги * толщину дороги см * массу 1 кв м дороги толщиной 1 см"""
        return super().square() * self._thickness * self.__mass_per_meter


length = 20  # m
width = 5000  # m
thickness = 5  # cm

r = MassCount(length, width, thickness)
print(r.mass() / 1000, "т")
