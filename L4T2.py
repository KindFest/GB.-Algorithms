# Урок 4. Практическое задание 2.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого
# числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

# Представлено 2 варианта решения задачи. Если смотреть на результаты замеров timeit, то можно
# сделать вывод, что в обоих случаях зависимость линейная. Также на первый взгляд кажется,
# что 2е решение лучше.
# Однако при поиске простого числа с порядковым номером от ~4000 2е решение
# начнает проигрывать по скорости. И чем больше порядковый номер, тем больше проигрыш.
# Таким образом, становится понятно, что зависимость как минимум 2-го решения не линейная. При
# увеличении N в 2 раза время увеличивается в ~3 раза. Все дело в строке:
# for j in range(2, i // 2):
# Таким образом можно объяснить пересечение графиков при больших N (то есть 1й
# алгоритм начинает работать быстрее).
#
# PS: На просторах интернета нашел алгоритм, который в разы быстрее Решето при больших N,
# однако так как он не является моим решением, то не привожу его тут :)

import timeit
import cProfile

# 1й вариант решения. Решето.

def sieve(n):
    sieve_lst = [i for i in range(n * 1000)]
    sieve_lst[1] = 0
    for i in range(2, n * 1000):
        if sieve_lst[i] != 0:
            j = i * 2
            while j < n * 1000:
                sieve_lst[j] = 0
                j += i
    res = [i for i in sieve_lst if i != 0]
    return res[n - 1]


print(timeit.timeit('sieve(4)', number=100, globals=globals())) # 0.20308610000000002
print(timeit.timeit('sieve(8)', number=100, globals=globals())) # 0.41616
print(timeit.timeit('sieve(16)', number=100, globals=globals())) # 0.8044475000000001
print(timeit.timeit('sieve(32)', number=100, globals=globals())) # 1.7201164

cProfile.run('sieve(4)')
#       6 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1    0.003    0.003    0.003    0.003 L4T2.py:14(sieve)
#      1    0.000    0.000    0.000    0.000 L4T2.py:15(<listcomp>)
#      1    0.000    0.000    0.000    0.000 L4T2.py:23(<listcomp>)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve(8)')
# 6 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 L4T2.py:14(sieve)
#         1    0.000    0.000    0.000    0.000 L4T2.py:15(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L4T2.py:23(<listcomp>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve(16)')
# 6 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.006    0.006    0.007    0.007 L4T2.py:14(sieve)
#         1    0.001    0.001    0.001    0.001 L4T2.py:15(<listcomp>)
#         1    0.000    0.000    0.000    0.000 L4T2.py:23(<listcomp>)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve(32)')
#       6 function calls in 0.014 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#      1    0.012    0.012    0.014    0.014 L4T2.py:14(sieve)
#      1    0.001    0.001    0.001    0.001 L4T2.py:15(<listcomp>)
#      1    0.001    0.001    0.001    0.001 L4T2.py:23(<listcomp>)
#      1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2й вариант решения.


def prime(n):
    if n == 1:
        return 2
    ind = 0
    num_lst = [i for i in range(3, n * 1000, 2)]
    for i in num_lst:
        for j in range(2, i // 2):
            if i % j == 0:
                break
        else:
            ind += 1
        if ind + 1 == n:
            return i


print(timeit.timeit('prime(4)', number=100, globals=globals())) # 0.010761800000000044
print(timeit.timeit('prime(8)', number=100, globals=globals())) # 0.020787599999999795
print(timeit.timeit('prime(16)', number=100, globals=globals())) # 0.04063339999999993
print(timeit.timeit('prime(32)', number=100, globals=globals())) # 0.07889370000000007

cProfile.run('prime(4)')
   #       5 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 L4T2.py:90(prime)
   #      1    0.000    0.000    0.000    0.000 L4T2.py:95(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(8)')
   #       5 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 L4T2.py:90(prime)
   #      1    0.000    0.000    0.000    0.000 L4T2.py:95(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(16)')
   #       5 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 L4T2.py:90(prime)
   #      1    0.000    0.000    0.000    0.000 L4T2.py:95(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(32)')
   #       5 function calls in 0.001 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
   #      1    0.000    0.000    0.001    0.001 L4T2.py:90(prime)
   #      1    0.000    0.000    0.000    0.000 L4T2.py:95(<listcomp>)
   #      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

x = int(input('Введите порядковый номер простого числа: '))
prime_1 = sieve(x)
print(prime_1)
prime_2 = prime(x)
print(prime_2)
