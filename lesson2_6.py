# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 2, Задание 6
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#

#
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#

clear_screen = "\n" * 100

item_card = ("название", "цена", "количество", "единица измерения")
warehouse = list()

# предварительный данные для быстрого теста
# warehouse = [(1, {'название': 'qqqq', 'цена': 1.0, 'количество': 2.0, 'единица измерения': 'q'}), (2, {'название': 'wwww', 'цена': 3.0, 'количество': 33.0, 'единица измерения': 'w'}), (3, {'название': 'eeee', 'цена': 1.0, 'количество': 2.0, 'единица измерения': 'r'})]

while True:
    print(clear_screen+"1 - Добавить товар\n2 - Получить аналитику\n0 - Выход")
    user_choice = input("Что делаем?: ")
    if user_choice.isdecimal():
        menu_item = int(user_choice)
        if menu_item == 1:
            while True:
                # без проверки валидность ввода данных
                prod_name = input("Название товара: ")
                prod_price = float(input("Цена: "))
                prod_quantity = float(input("Количество: "))
                prod_dimension = input("Единица измерения: ")

                new_id = len(warehouse) + 1

                warehouse.append((new_id, {item_card[0]: prod_name, item_card[1]: prod_price, item_card[2]: prod_quantity, item_card[3]: prod_dimension}))

                more_choice = input("Еще один товар? (y/n): ")
                if more_choice != "y": break

        if menu_item == 2:
            result = dict()
            for i in item_card:
                result[i] = []
            for i in warehouse:
                for k in item_card:
                    result[k].append(i[1][k])

            # не убирал повторяющиеся единицы измерения, так как это не совсем логично

            print("исходные данные:")
            print(warehouse)
            #  print(*warehouse, sep="\n") вариант форматированного вывода
            print("результат анализа:")
            print(result)
            #  print(*result, sep="\n") вариант форматированного вывода
            input("\n>>> нажмите enter для возврата в меню\n")

        if menu_item == 0:
            break

    else:
        print("Введите 1, 2 или 0")
