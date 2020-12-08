# Урок 3. Практическое задание 7.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
# между собой (оба являться минимальными), так и различаться.
#
# Первый вариант решения с удалением минимального элемента в массиве, зато через рекурсию.

import random

START_POS = 1
END_POS = 10
MATR_ELEM = 10


def find_min(array, min_nums, i):
    min_num = END_POS
    for item in array:
        if min_num > item:
            min_num = item
    array.remove(min_num)
    min_nums.append(min_num)
    i -= 1
    if i == 0:
        return min_nums
    else:
        return find_min(array, min_nums, i)


matrix1 = [random.randint(START_POS, END_POS) for _ in range(MATR_ELEM)]
matrix2 = matrix1.copy() # Пришлось ввести копию массива, иначе первое решение его изменяет, а я
                         # хотел показать, что оба вариант выдают одинаковый ответ
                         # Но для меня осталось загадкой, почему меняется matrix1? То есть если
                         # раскоментировать print(matrix1), то будет распечатан массив из 8 чисел

print(f'Сгенерированный массив {matrix1}')
min_numbers = find_min(matrix1, [], 2)
print(f'Минимальными числами в сгенерированном массиве являются {min_numbers}')
# print(f'Сгенерированный массив {matrix1}')

# Второй вариант решения. Без удаления минимального элемента массива.

min_numbers = []
min_num = END_POS
min_pos = MATR_ELEM + 1
for i in range(2):
    for j, item in enumerate(matrix2, 1):
        if min_num >= item and min_pos != j:
            min_num = item
            if i == 0:
                min_pos = j
    min_numbers.append(min_num)
    min_num = END_POS
print(f'Сгенерированный массив {matrix2}')
print(f'Минимальными числами в сгенерированном массиве являются {min_numbers}')
