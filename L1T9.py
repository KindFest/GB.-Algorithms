# Урок 1. Практическое задание 9.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите 3 разных числа.')
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
if (a < b < c) or (c < b < a):
    print('B - среднее число')
elif (a < c < b) or (b < c < a):
    print('C - среднее число')
else:
    print('A - среднее число')
