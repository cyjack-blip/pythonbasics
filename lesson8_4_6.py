# -*- coding: utf-8 -*-
# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 8, Задание 4-6
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# 4
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#


class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


class NotInWarehouse(OwnException):
    pass


class NotEnough(OwnException):
    pass


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.balance = []

    def receive(self, equipment, quantity):
        if equipment in self.items:
            index = self.items.index(equipment)
            self.balance[index] = self.balance[index] + quantity
        else:
            self.items.append(equipment)
            self.balance.append(quantity)

    def giveaway(self, equipment, quantity):
        try:
            if equipment not in self.items:
                raise NotInWarehouse(equipment)
            index = self.items.index(equipment)
            if self.balance[index] < quantity:
                raise NotEnough(equipment)
            else:
                self.balance[index] -= quantity
        except NotInWarehouse:
            print(f"На этотм складе нет {equipment.name}")
        except NotEnough:
            print(f"На складе нет такого количества {equipment.name}")

    def transfer(self, equipment, quantity, other_store):
        self.giveaway(equipment, quantity)
        other_store.receive(equipment, quantity)

    def __str__(self):
        store_list = f"Склад {self.name}:\n"
        if self.items:
            for i, item in enumerate(self.items):
                store_list += f"{i+1}: {item}: {self.balance[i]}\n"
        else:
            store_list += "пусто"
        return store_list


class OfficeEquipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, цена {self.price}"


class Printer(OfficeEquipment):
    def __init__(self, name, price, color=False):
        super().__init__(name, price)
        self.color = color

    def __repr__(self):
        s = super().__str__()
        return f"{s}, цветной: {self.color}"


class Scanner(OfficeEquipment):
    def __init__(self, name, price, dpi):
        super().__init__(name, price)
        self.dpi = dpi

    def __repr__(self):
        s = super().__str__()
        return f"{s}, разрешение сканера: {self.dpi}"


class Xerox(OfficeEquipment):
    def __init__(self, name, price, speed):
        super().__init__(name, price)
        self.speed = speed

    def __repr__(self):
        s = super().__str__()
        return f"{s}, скорость копирования: {self.speed}"


# инициализация складов
warehouse_1 = Store("main")
warehouse_2 = Store("other")

# инициализация офисной техники
# название, цена, сппециальное свойство
printer_1 = Printer("Принтер", 100, True)
scanner_1 = Scanner("Сканер", 300, 1400)
scanner_2 = Scanner("Сканер2", 230, 700)
xerox_1 = Xerox("Ксерокс", 200, 10)
xerox_2 = Xerox("Ксерокс2", 200, 10)

# посмотрим что у нас за техника получилась (тест __repr__)
print(printer_1, scanner_1, scanner_2, xerox_1, xerox_2, " ", sep="\n")

# примем на склад технику - наименование, количество
warehouse_1.receive(printer_1, 10)
warehouse_1.receive(scanner_1, 2)
warehouse_2.receive(scanner_2, 2)
warehouse_1.receive(xerox_1, 1)
warehouse_1.receive(xerox_2, 1)
warehouse_1.receive(xerox_2, 1000)

# что у нас на складах получилось
print(warehouse_1)
print(warehouse_2)

# передадим технику куда-нибудь во вне, техниика, количество
warehouse_1.giveaway(xerox_2, 10)

# переместим с одного слада n штук на другой слкда
warehouse_1.transfer(xerox_2, 5, warehouse_2)

# что у нас на складах получилось
print(warehouse_1)
print(warehouse_2)

# попробуем перемемститьт больше, чем есть на складе
warehouse_1.transfer(xerox_2, 1000, warehouse_2)

# попрробуем переместить то, чего нет на складе
warehouse_1.transfer(scanner_2, 1000, warehouse_2)
