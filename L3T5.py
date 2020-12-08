# Урок 3. Практическое задание 5.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию
# в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

START_POS = -10
END_POS = 10
MATR_ELEM = 10

matrix = [random.randint(START_POS, END_POS) for _ in range(MATR_ELEM)]
print(f'Сгенерированный массив {matrix}')
max_num = 0
for item in matrix:
    if max_num == 0 and item < 0:
        max_num = item
    elif max_num < item < 0:
        max_num = item
print(f'Максимальное отрицательное число в массиве = {max_num}')
