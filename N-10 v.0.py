def DIV_NN_Dk(n1, arr1, n2, arr2):
    num = 0
    num_list = []
    temp = []
    chk = COM_NN_D(n1, arr1, n2, arr2)
    if chk == 2:
        min_num = arr2
        n2 = len(min_num)
        max_num = arr1
    elif chk == 1:
        min_num = arr1
        n2 = len(min_num)
        max_num = arr2
    else:
        return [1, [1]]      # Если число делится само на себя, k = 1

    # Минимальное не должно быть равно 0
    if not sum(min_num):
        raise ZeroDivisionError

    # Если нужно найти первую цифру деления на 1
    if sum(min_num) == 1:
        num_list.append(max_num[0])
        return MUL_Nk_N(1, num_list, len(max_num) - 1)

    # Берём у большего числа цифры для деления на меньшее
    for i in range(len(min_num)):
        temp.append(max_num[i])

    n_temp = len(temp)

    # Если цифр для деления на меньшее не хватило, возьмём ещё одну
    if COM_NN_D(n_temp, temp, n2,  min_num) == 1:
        temp.append(max_num[n_temp])
        n_temp += 1

    k = len(max_num) - n_temp

    # Деление в столбик
    while COM_NN_D(n_temp, temp, n2,  min_num) != 1:
        sub = int(''.join(map(str, temp))) - int(''.join(map(str, min_num)))
        temp = list(map(int, str(sub)))
        n_temp = len(temp)
        num += 1

    return [num, k]
