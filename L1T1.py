# Ссылка на блок схему:
# https://drive.google.com/file/d/1QJcfnhL0-iC9sqLymKeh1doZJ4PKag2p/view?usp=sharing
#
# Урок 1. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите число от 100 до 999: '))
a = x // 100
b = x // 10 % 10
c = x % 100 % 10
y = a + b + c
z = a * b * c
print(f'Сумма цифр введенного числа = {y}, а произведение = {z}')