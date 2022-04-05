# N-7 Умножение натурального числа на 10^k
# автор: Пелагейко Анастасия 1310

# функция получает на вход номер старшей позиции в натуральном числе (кол-во цифр в числе) 'n'
# массив (список) цифр в натуральном числе 'А' и степень десятки 'k'

# умножить натуральное число на 10^k - значит приписать к этому числу k нулей справа

def MUL_Nk_N(n, A, k):
    # заполняем элементы списка нулями, начиная с n-ного элемента и заканчивая n+k
    # т.к. итоговое число будет содержать в себе n+k элементов
    for i in range(n, n + k):
        A.insert(i, 0)
    # увеличиваем счётчик кол-ва цифр
    n += k
    # имеем число n и список А, содержащий в себе число, умноженное на 10^k и разбитое на цифры
    return n, A






