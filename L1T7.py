# Урок 1. Практическое задание 7.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# По длинам трех отрезков, введенных пользователем, определить возможность существования
# треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

print('Введите длины трех отрезков')
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
if ((a + b) > c) and ((a + c) > b) and ((c + b) > c):
    if a == b == c:
        print('Треугольник равносторонний')
    elif (a == b) or (a == c) or (b == c):
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника с введенными длинами не существует')
