# Задача Z-4
# Выполнил Смирнов М.О.

# Входные данные:
# Программа принимает на вход натуральное число, массив N[n; A[]],
# где n - номер старшей позиции в числе, A[] - массив цифр.

# Алгоритм:
# Программа приводит тип к целочисленному числу, массиву N[b, n; A[]],
# где b - знак, n - номер старшей позиции в числе, A[] - массив цифр.

# Выходные данные:
# Программа возвращает целочисленное значение N[0, n; A[]]
def TRANS_N_Z(N):
    Z = [0, N[0], N[1]]
    return Z