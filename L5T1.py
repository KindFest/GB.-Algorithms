# Урок 5. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для
# всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и
# ниже среднего.

import collections


profit = []
info = {}
profit_total = 0
quantity = int(input('Введите количество предприятий: '))
Enterprises = collections.namedtuple('Enterprises', 'name, Q1, Q2, Q3, Q4, total')
for i in range(quantity):
    name = input(f'Введите название {i+1}го предприятия: ')
    for j in range(1, 5):
        profit.append(float(input(f'Прибыль за {j} квартал: ')))
    total_sum = sum(profit)
    enterprise = Enterprises(name, profit[0], profit[1], profit[2], profit[3], total_sum)
    info.update({i: enterprise})
    profit_total += total_sum
    profit.clear()
profit_avg = profit_total / quantity
print(f'Средняя прибыль всех предприятий = {profit_avg}')
other_avg = []
below_avg = []
for i in range(len(info)):
    if info[i].total >= profit_avg:
        other_avg.append(info[i].name)
    else:
        below_avg.append(info[i].name)
print(f'Предприятия с прибылью выше среднего: {other_avg}')
print(f'Предприятия с прибылью ниже среднего: {below_avg}')
