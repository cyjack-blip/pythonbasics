# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 6, Задание 4
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
#

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} - поехали'

    def stop(self):
        return f'{self.name} - остановилась'

    def turn(self, direction):
        return f'{self.name} поворачивает {direction}'

    def show_speed(self):
        return f'У {self.name} скорость {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной'
        else:
            return f'Скорость {self.name} нормальная'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.speed} - превышениие!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская мамшина'
        else:
            return f'{self.name} - не полицейская мамшина'


toyota = SportCar(100, 'Красный', 'Тойота')
hyundai = TownCar(30, 'Белый', 'Хэндай')
porter = WorkCar(70, 'Зеленый', 'Портер')
ford = PoliceCar(110, 'Голубой',  'Форд', True)

print(porter.turn("налево"))
print(f'Вначале {hyundai.turn("направо")}, а {toyota.stop()}')
print(f'{porter.go()}!  {porter.show_speed()}')
print(f'{porter.name} цвет - {porter.color}')
print(f'{toyota.name} Полицейскакя мамшина? {toyota.is_police}')
print(f'{porter.name} Полицейская мамшина? {porter.is_police}')
print(f'{ford.name} Полицейскакя мамшина? {ford.is_police}')

print(toyota.show_speed())
print(hyundai.show_speed())
print(ford.police())
print(ford.show_speed())
