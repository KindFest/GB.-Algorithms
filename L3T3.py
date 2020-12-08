# Урок 3. Практическое задание 3.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

START_POS = 1
END_POS = 100
MATR_ELEM = 10

matrix = [random.randint(START_POS, END_POS) for _ in range(MATR_ELEM)]
print(f'Сформированный массив: {matrix}')
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
matrix.pop(max_pos)
matrix.insert(max_pos, min_num)
matrix.pop(min_pos)
matrix.insert(min_pos, max_num)
print(f'Массив после замены максимального и минимального чисел {matrix}')
