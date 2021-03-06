# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 3, Задание 5
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
#

def my_sum(*args):
    my_total = 0
    for x in args:
        if x != 'q':
            try:
                my_total += float(x)
            except ValueError:
                print("Вы ввели не число, но и не символ завершения, пропускакем...")
        else:
            break
    return my_total


print("Введите числа, разделенные пробелами\nСимвол q в любом месте для завершения")
total = 0

while True:
    input_num = input("Ввдите числа: ").split()
    last = my_sum(*input_num)

    total += last
    print(f"last {last} (total {total}) ")

    if input_num.count('q'):
        break
