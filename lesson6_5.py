# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 6, Задание 5
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


# частичное переопределение метода
class Brush(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. ')
        super().draw()


# с переопределением метотда
class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Пишем текст ручкой')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Рисуем скетч карандашом')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Выделяем текст маркером')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
brush = Brush('Кистотчка')

pen.draw()
pencil.draw()
handle.draw()
brush.draw()
