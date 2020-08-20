# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 3, Задание 6
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
#

def int_func(mstr):
    # Если ближе к теме урока, то так (но есть .capitalize() или даже .title() для целой строки)
    return chr(ord(mstr[0])-32)+mstr[1:]


flag = True

print("Введите quit для завершения")
# программа будет пропускать слова с ошибками и изменять первую букву только у правильных слов
while flag:
    result_string = ""
    user_string = input("Введите несколько слов, разделенных пробелами. \
Слова должны состоять только из маленьких латинских букв: ").split()

    if user_string.count('quit'):
        break

    for a in user_string:
        for i in a:
            if ord(i) not in range(97, 123):
                flag = False
        if flag:
            result_string += int_func(a)+" "
        else:
            result_string += "!error! "
            flag = True

    print(result_string)
