# Урок 3. Практическое задание 6.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

START_POS = 1
END_POS = 10
MATR_ELEM = 10

matrix = [random.randint(START_POS, END_POS) for _ in range(MATR_ELEM)]
print(f'Сгенерированный массив {matrix}')
max_num = START_POS
max_pos = 0
min_num = END_POS
min_pos = 0
for i, item in enumerate(matrix):
    if item > max_num:
        max_num = item
        max_pos = i
    if item < min_num:
        min_num = item
        min_pos = i
print(f'Максимальное число {max_num} находится на позиции {max_pos}, '
      f'минимальное число {min_num} находится на позиции {min_pos}')
amount = 0
if min_pos > max_pos:
    min_pos, max_pos = max_pos, min_pos
for i in range(min_pos+1, max_pos):
    amount += matrix[i]
print(f'Сумма между этими числами = {amount}')
