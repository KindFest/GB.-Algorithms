# Урок 6. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

import random
import sys

START_POS = 1
END_POS = 100


def find_min1(array, min_nums, i):
    """
    Первый вариант решения. С удалением минимального элемента массива. Рекурсия.
    array - массив, в котором ищем минимальное число
    min_nums - массив, в который помещаем найденные минимальные числа
    i - количество минимальных чисел, которые надо найти.
    """
    array_1 = array[:]
    min_num = array_1[0]
    for j in range(1, len(array_1)):
        if min_num > array_1[j]:
            min_num = array_1[j]
    array_1.remove(min_num)
    min_nums.append(min_num)
    i -= 1
    if i == 0:
        return min_nums, memory_usage(locals().copy()) + main_elems_mem
    else:
        return find_min1(array_1, min_nums, i)


def find_min2(array):
    """
    Второй вариант решения. Без удаления минимального элемента массива.
    array - массив, в котором ищем минимальное число
    """
    array_1 = array[:]
    min_nums = []
    min_num = END_POS
    min_pos = len(array_1) + 1
    for i in range(2):
        for j, item in enumerate(array_1, 1):
            if min_num >= item and min_pos != j:
                min_num = item
                if i == 0:
                    min_pos = j
        min_nums.append(min_num)
        min_num = END_POS
    return min_nums, memory_usage(locals().copy()) + main_elems_mem


def find_min3(array):
    """
    Третий вариант решения. С использованием стандартных функций.
    array - массив, в котором ищем минимальное число
    """
    array_1 = array[:]
    min_nums = [min(array_1)]
    array_1.remove(min_nums[0])
    min_nums.append(min(array_1))
    return min_nums, memory_usage(locals().copy()) + main_elems_mem


def memory_usage(loc_dct):
    # формируем словарь переменных в loc_dct с исключением модулей, функций и служебных переменных
    loc_dct = {key: val for key, val in loc_dct.items() if isinstance(val, list) or isinstance(val, int)}
    mem_size = 0
    for elem in loc_dct:
        mem_size += sys.getsizeof(loc_dct[elem])
        if isinstance(loc_dct[elem], list):
            for k in loc_dct[elem]:
                mem_size += sys.getsizeof(k)
    return mem_size


matrix = ([random.randint(START_POS, END_POS) for _ in range(10)])
main_elems_mem = memory_usage(globals().copy())
print(f'Память под глобальные переменные: {main_elems_mem}')
print(f'Сгенерированный список для контроля правильности решения: \n{matrix}')
print(f'Метод 1. Минимальные значения: {find_min1(matrix, [], 2)[0]}. Использовано памяти: {find_min1(matrix, [], 2)[1]}')
print(f'Метод 2. Минимальные значения: {find_min2(matrix)[0]}. Использовано памяти: {find_min2(matrix)[1]}')
print(f'Метод 3. Минимальные значения: {find_min3(matrix)[0]}. Использовано памяти: {find_min3(matrix)[1]}')

# Исходя из приведенных расчетов получается, что 1й вариант решения экономичнее остальных.
# ----------------------
# Память под глобальные переменные: 520
# Сгенерированный список для контроля правильности решения:
# [96, 6, 4, 80, 40, 88, 11, 33, 19, 88]
# Метод 1. Минимальные значения: [4, 6]. Использовано памяти: 1484
# Метод 2. Минимальные значения: [4, 6]. Использовано памяти: 1684
# Метод 3. Минимальные значения: [4, 6]. Использовано памяти: 1524
# ----------------------
# Однако есть один нюанс. Так как в первом варианте использована рекурсия, то при вызове функции
# по расчету использованной памяти memory_usage в нее передается список после удаления пары
# элементов. Я нивелировал этот момент для 2го и 3го решения, путем ввода дополнительного списка
# array_1 (необязательного), однако для рекурсии сделать это не смог (с условием сохранения простоты
# подсчета затрат памяти (уверен, что есть способ проще, но я пока не придумал как).
# Элементарный анализ кода показывает, что наиболее экономичный с точки зрения памяти - 3й метод:
# там использовано меньше переменных. Но там же используется встроенная функция min, которая также
# использует память :).
