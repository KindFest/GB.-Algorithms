# Урок 3. Практическое задание 8.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна
# вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

def row_former(date):
    loc_sum = 0
    one_row = date.split(' ')
    for i in range(len(one_row)):
        one_row[i] = int(one_row[i])
        loc_sum += one_row[i]
    one_row.append(loc_sum)
    return one_row


def matrix_print(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(f'{array[i][j]:>7}', end='')
        print()


matrix = []
for i in range(5):
    row = input(f'Введите 3 числа через пробел для строки {i+1}: ')
    matrix.append(row_former(row))

matrix_print(matrix)
