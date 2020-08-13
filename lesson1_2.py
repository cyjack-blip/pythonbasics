# Домашняя работа по курсу Основы языка Python 10.08.2020
# Урок 1, Задание 2
# Выполнил: Евгений Иванов
# https://www.facebook.com/evgeniy.ivanov/
#

#
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
#

secondsPerMin = 60
secondsPerHour = 3600

seconds = int(input("Введите количество секунд (число): "))
hh = seconds // secondsPerHour
mm = (seconds - hh * secondsPerHour) // secondsPerMin
ss = (seconds - hh * secondsPerHour - mm * secondsPerMin)
print(f"Получите время (чч:мм:сс): {hh:02d}:{mm:02d}:{ss:02d}")
