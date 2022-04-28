# Урок 2. Практическое задание 9.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Посчитать, сколько раз встречается определен

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран
# это число и сумму его цифр.

def amount_digit(y):
    if y // 10 == 0:
        return y % 10
    return y % 10 + amount_digit(y // 10)


print('Поиск чисел с максимальной суммой цифр. Выход - "0"')
number = 0
digit_amount = 0
while True:
    x = int(input('Введите число: '))
    if x != 0:
        temp_amount = amount_digit(x)
    else:
        break
    if temp_amount > digit_amount:
        digit_amount = temp_amount
        number = x
print(f'Среди введенных чисел в числе {number} наибольшая сумма цифр {digit_amount}')
