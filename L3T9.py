# Урок 3. Практическое задание 9.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_M = 4
SIZE_N = 6
MIN_ITEM = 0
MAX_ITEM = 1000


def matrix_print(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(f'{array[i][j]:>7}', end='')
        print()


min_list = []
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]
for j in range(len(matrix[1])):
    min_num = MAX_ITEM
    for i in range(len(matrix)):
        if matrix[i][j] < min_num:
            min_num = matrix[i][j]
    min_list.append(min_num)
max_num = MIN_ITEM
for item in min_list:
    if item > max_num:
        max_num = item
print(f'Сгененированный массив: ')
matrix_print(matrix)
print(f'Минимальные числа по столбцам: {min_list}')
print(f'Максимальное число среди минимальных = {max_num}')
