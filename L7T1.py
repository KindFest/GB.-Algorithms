# Урок 7. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный
# массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка
# пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random


def bubble_sort(arr):
    """
    Одно улучшение находится элементарно, а вот второе так и не нашел :(
    """
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1


array = [random.randint(-100, 99) for i in range(10)]
print(array)
bubble_sort(array)
print(array)
