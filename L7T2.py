# Урок 7. Практическое задание 2.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr):
    """
    Буду честен: залез на Вики, прочитал про сортировку слиянием. Алгоритм более-менее понятен, встал
    вопрос реализации. Но на самой Вики был код реализации, в том числе и на python.
    Взял его как пример и начал разбираться. Мне он показался не рабочим, ибо происходит постоянная
    сортировка вновь объединяемых массивов, а не объединение уже отсортированных (хотя по факту они
    уже отсортированы).
    В итоге решил реализовать этот метод сортировки как понял его сам на основе описания алгоритма.
    Решение предоставлено ниже.

    PS: Думал прицепить сюда же решение из Вики для вашего внимания, но, думаю, вы его и сами видели :)
    PS: Использовал комментарий типа doc, чтобы текст был виден на фоне условий задачи.
    """
    def merge_lst(arr_1, arr_2):
        arr_res = []
        last_index = len(arr_1) + len(arr_2)
        j = 0
        k = 0
        for i in range(last_index):
            if j == len(arr_1):
                for k in range(k, len(arr_2)):
                    arr_res.append(arr_2[k])
                break
            elif k == len(arr_2):
                for j in range(j, len(arr_1)):
                    arr_res.append(arr_1[j])
                break
            elif arr_1[j] < arr_2[k]:
                arr_res.append(arr_1[j])
                j += 1
            elif arr_1[j] >= arr_2[k]:
                arr_res.append(arr_2[k])
                k += 1
        return arr_res

    count = len(arr)
    if count > 2:
        part_1 = merge_sort(arr[:count // 2])
        part_2 = merge_sort(arr[count // 2:])
        arr = merge_lst(part_1, part_2)
    elif len(arr) > 1 and arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    return arr


array = [random.random() * (0 - 50) + 50 for i in range(10)]
print(array)
print(merge_sort(array))
