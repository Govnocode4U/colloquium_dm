# Задача P-5: Старший коэффициент многочлена
# Выполнил Егоров И.М

# Входные данные:
# Программа принимает на вход C - массив коэффициентов многочлена, который выглядит следующим образом:
# Пример многочлена: 2x^2 + 3x + 5 - это C[2, 3, 5]
#  То есть массив коэффициентов начинается с наибольшей степени многочлена

# Алгоритм:
# Получаем на вход массив коэффициентов и возвращаем первый коэффициент (нулевой элемент массива)

# Выходные данные:
# Возвращаем переменную coefficient - старший коэффициент многочлена.

C = [[1,5], [2,[4,3]], [1,[2]], [1,[0]], [1,[1]]
def LED_P_Q(C):
    coefficient = C[0]
    return [coefficient]
print(LED_P_Q(C))

    
