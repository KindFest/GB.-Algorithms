# Урок 8. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Алгоритмы и структуры данных на Python. Базовый курс
# Факультет: Geek University Python-разработки
#
# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции
# дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9
import hashlib


def substr_count_1(my_str):
    """
    Решение с использованием hash функции
    """
    result = []
    i = len(my_str)
    lenght = len(my_str)
    while i > 0:
        for j in range(lenght - i + 1):
            if hashlib.sha256(my_str[j:j + i].encode('utf-8')).hexdigest() not in result:
                result.append(hashlib.sha256(my_str[j:j + i].encode('utf-8')).hexdigest())
        i -= 1
    return len(result) - 1


def substr_count_2(my_str):
    """
    Решение с использованием set (ибо set использует hash)
    """
    result = set()
    i = len(my_str)
    lenght = len(my_str)
    while i > 0:
        for j in range(lenght - i + 1):
            result.add(my_str[j:j + i])
        i -= 1
    return len(result) - 1


my_string = 'sova'
print(f'Количество уникальных подстрок в строке {my_string} = {substr_count_1(my_string)}')
print(f'Количество уникальных подстрок в строке {my_string} = {substr_count_2(my_string)}')
