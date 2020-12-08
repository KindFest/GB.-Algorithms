# Урок 3. Практическое задание 2.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить
# значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях
# первого массива стоят четные числа.

# Также 2 решения: с использованием функци range и enumerate

import random

START_POS = 1
END_POS = 100
MATR_ELEM = 10

matrix = [random.randint(START_POS, END_POS) for _ in range(MATR_ELEM)]

# Первое решение

even_pos = list()
for i in range(len(matrix)):
    if matrix[i] % 2 == 0:
        even_pos.append(i)
print(f'В массиве {matrix} четные числа находятся на {even_pos} позициях.')

# Второе решение

even_pos = list()
for i, item in enumerate(matrix):
    if item % 2 == 0:
        even_pos.append(i)
print(f'В массиве {matrix} четные числа находятся на {even_pos} позициях.')
