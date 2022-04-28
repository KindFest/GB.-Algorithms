# Урок 3. Практическое задание 4.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Определить, какое число в массиве встречается чаще всего.

import random

START_POS = 1
END_POS = 10
MATR_ELEM = 10

matrix = [random.randint(START_POS, END_POS) for _ in range(MATR_ELEM)]
print(f'{matrix=}')
result_dict = {}
for item in matrix:
    if result_dict.get(item):
        result_dict[item] += 1
    else:
        result_dict[item] = 1
print(f'{result_dict=}')
max_quantity = 0
number = 0
for key, val in result_dict.items():
    if max_quantity < val:
        max_quantity = val
print(f'Число ', end='')
for key, val in result_dict.items():
    if val == max_quantity:
        print(f'{key}, ', end='')
print(f' встречается {max_quantity} раз')
