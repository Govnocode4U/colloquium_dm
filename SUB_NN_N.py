"""
N-5
Выполнил Шаров Антон
Алгоритм: аналогичен вычитанию столбиком

В случае, когда первое число меньше второго (что противоречит условию), функция вернёт (0, [])
"""


def SUB_NN_N(n1: int, a1: list, n2: int, a2: list) -> tuple:
    """
    N-5. Вычитание из первого большего натурального числа второго меньшего или равного

    :param n1: Длина перового числа
    :param a1: Первое число
    :param n2: Длина второго числа
    :param a2: Второе число

    :return: Разность чисел в виде натурального числа - (длина, число)
    """
    res = []  # Итоговое число
    eq = COM_NN_D(n1, a1, n2, a2)  # Для начала сравним входные числа (Нужна функция из N-1) (Здесь мог бы быть match case)
    if eq == 0:  # Случай, когда входные числа равны
        res.append(0)  # Итоговое число 0
    elif eq == 2:  # Случай, когда первое входное число больше второго
        for i in range(1, n1 + 1):  # Пройдём от последних цифр чисел до первых
            # Имитация вычитания столбиком
            if i <= n2:
                if a1[n1 - i] >= a2[n2 - i]:
                    res.append(a1[n1 - i] - a2[n2 - i])
                else:
                    a1[n1 - i - 1] -= 1
                    res.append(a1[n1 - i] - a2[n2 - i] + 10)
            else: res.append(a1[n1 - i])
        res.reverse()

        while res[0] == 0: res.pop(0)  # Уберём незначащие нули в начале

    return len(res), res


# Пример 1. 222 - 184
print(SUB_NN_N(3, [2, 2, 2], 2, [1, 8]))  # (3, [2, 0, 4])

# Пример 2. 222 - 222
print(SUB_NN_N(3, [2, 2, 2], 3, [2, 2, 2]))  # (1, [0])
