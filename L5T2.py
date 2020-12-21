# Урок 5. Практическое задание 2.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и
# C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections
HEX2DEC = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, }
DEC2HEX = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
           10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', }


def converting(r):
    delta = 0
    for i in range(len(r)):
        if r[i] + delta <= 15:
            r[i] = DEC2HEX[r[i] + delta]
            delta = 0
        else:
            r[i] = DEC2HEX[r[i] + delta - 16]
            delta = 1
    else:
        if delta == 1:
            r.append('1')
    r.reverse()
    return r


def calculation(num_1, num_2):
    res = collections.deque()
    for i in range(1, len(num_1) + 1):
        if len(num_2) >= i:
            res.append(HEX2DEC[num_1[-i]] + HEX2DEC[num_2[-i]])
        else:
            res.append(HEX2DEC[num_1[-i]])
    return converting(res)


def multiplier(num):
    num_mult = 0
    num.reverse()
    for i in range(len(num)):
        num_mult += HEX2DEC[num[i]] * 16 ** i
    return num_mult


result_mult = collections.deque()
number_1 = collections.deque(input('Введите 1-е число: ').upper())
number_2 = collections.deque(input('Введите 2-е число: ').upper())
if len(number_1) < len(number_2):
    number_1, number_2 = number_2, number_1
result_add = calculation(number_1, number_2)
result_mult = calculation(number_1, number_1)
for _ in range(multiplier(number_2) - 2):
    result_mult = calculation(result_mult, number_1)
print(f'Введенные числа: 1 = {number_1}, 2 = {number_2}')
print(f'Сумма чисел = {result_add}')
print(f'Произведение чисел = {result_mult}')
