# Урок 4. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
#  Проанализировать скорость и сложность одного любого алгоритма из разработанных
#  в рамках домашнего задания первых трех уроков.
#
# Урок 3. Задание 7.
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
# между собой (оба являться минимальными), так и различаться.
#
# Выводы: очевидно, что лучшая реализация - это Вариант 3: использование функции min из стандартной
# библиотеки Python. Данная реализация демонстрирует линейную зависимость.
# Два других решения, на мой взгляд, также демонстрируют линейную зависимость, однако реализация
# не так эффективна как у min. Скорость выполнения заметно ниже, при чем 2-е решение проигрывает
# первому.
# Также, с моей точки зрения, анализ cProfile не выявил проблем.
#
# PS: Также решил проанализировать вариант из вашего разбора ПЗ. Результат по быстродействию
# оказался худшим из всех рассмотренных. И это удивило, так как с виду ваш алгоритм выглядит проще.
# Привожу результаты здесь только для справки:
# 10 	 0.0048319
# 100 	 0.029200900000000002
# 1000 	 0.21227649999999998
# 10000  2.0072763
# 100000 21.6838937


import random
import timeit
import cProfile

START_POS = 1
END_POS = 100


def find_min1(array, min_nums, i):
    """
    Первый вариант решения. С удалением минимального элемента массива. Рекурсия.
    array - массив, в котором ищем минимальное число
    min_nums - массив, в который помещаем найденные минимальные числа
    i - количество минимальных чисел, которые надо найти.
    """
    array = array[:]
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
        return find_min1(array, min_nums, i)


def find_min2(array):
    """
    Второй вариант решения. Без удаления минимального элемента массива.
    array - массив, в котором ищем минимальное число
    """
    array = array[:]
    min_nums = []
    min_num = END_POS
    min_pos = len(array) + 1
    for i in range(2):
        for j, item in enumerate(array, 1):
            if min_num >= item and min_pos != j:
                min_num = item
                if i == 0:
                    min_pos = j
        min_nums.append(min_num)
        min_num = END_POS
    return min_nums


def find_min3(array):
    """
    Третий вариант решения. С использованием стандартных функций.
    array - массив, в котором ищем минимальное число
    """
    array = array[:]
    min_nums = []
    min_nums.append(min(array))
    array.remove(min_nums[0])
    min_nums.append(min(array))
    return min_nums


matr_elem = [10, 100, 1000, 10000, 100000]
for k in matr_elem:
    matrix = ([random.randint(START_POS, END_POS) for _ in range(k)])
    print(f'1 {k:>10}', '\t', timeit.timeit('find_min1(matrix, [], 2)', number=1000, globals=globals()))
    print(f'2 {k:>10}', '\t', timeit.timeit('find_min2(matrix)', number=1000, globals=globals()))
    print(f'3 {k:>10}', '\t', timeit.timeit('find_min3(matrix)', number=1000, globals=globals()))
    cProfile.run('find_min1(matrix, [], 2)')
    cProfile.run('find_min2(matrix)')
    cProfile.run('find_min3(matrix)')

# Результаты
#
# Timeit
#
# Вариант 1. Рекурсия               Вариант 2. Перебор              Вариант 3.
# с удалением элемента              без удаления элемента           Использование min
# 10 	 0.0022312999999999986      0.0036490999999999954           0.002108699999999998
# 100 	 0.010462500000000007       0.012153499999999998            0.0039073000000000024
# 1000 	 0.0865693                  0.14437250000000001             0.04648530000000001
# 10000  0.8279679999999999         1.3953195000000003              0.34039439999999965
# 100000 9.3273944                  14.8460397                      3.3880336
#
# -------------------------------------------------------------------------------------
#
# cProfile
#
# Вариант 1. Рекурсия с удалением элемента
#
# N = 10
#
# 9 function calls (8 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       2/1    0.001    0.000    0.001    0.001 L4T1.py:17(find_min1)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# N = 100
#
#       9 function calls (8 primitive calls) in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#    2/1    0.000    0.000    0.000    0.000 L4T1.py:17(find_min1)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# N = 1_000
#
#          9 function calls (8 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       2/1    0.000    0.000    0.000    0.000 L4T1.py:17(find_min1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# N = 10_000
#
#          9 function calls (8 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       2/1    0.001    0.000    0.001    0.001 L4T1.py:17(find_min1)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# N = 100_000
#          9 function calls (8 primitive calls) in 0.016 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#       2/1    0.015    0.007    0.015    0.015 L4T1.py:17(find_min1)
#         1    0.001    0.001    0.016    0.016 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# -------------------------------------------------------------------------------------
#
# Вариант 2. Перебор с удалением элемента
#
# N = 10
#
#      7 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 L4T1.py:38(find_min2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# N = 100
#
#      7 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 L4T1.py:38(find_min2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# N = 1_000
#
#     7 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 L4T1.py:38(find_min2)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# N = 10_000
#
#      7 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.001    0.001    0.001    0.001 L4T1.py:38(find_min2)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# N = 100_000
#
#       7 function calls in 0.015 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#      1    0.015    0.015    0.015    0.015 L4T1.py:38(find_min2)
#      1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# -------------------------------------------------------------------------------------
#
# Вариант 3. Использование min
#
# N = 10
#
#          9 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 L4T1.py:58(find_min3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# N = 100
#
#       9 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 L4T1.py:58(find_min3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# N = 1_000
#
#       9 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 L4T1.py:58(find_min3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# N = 10_000
#
#      9 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 L4T1.py:58(find_min3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#
# N = 100_000
#
#       9 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.000    0.000    0.003    0.003 L4T1.py:58(find_min3)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      2    0.003    0.001    0.003    0.001 {built-in method builtins.min}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}



# matr_elem = int(input('Введите количество элементов массива: '))
# matrix = [random.randint(START_POS, END_POS) for _ in range(matr_elem)]
# print(f'Сгенерированный массив {matrix}')
# min_numbers = find_min1(matrix, [], 2)
# print(f'Решение 1: Минимальными числами в сгенерированном массиве являются {min_numbers}')
# min_numbers = find_min2(matrix)
# print(f'Решение 2: Минимальными числами в сгенерированном массиве являются {min_numbers}')
# min_numbers = find_min3(matrix)
# print(f'Решение 3: Минимальными числами в сгенерированном массиве являются {min_numbers}')
