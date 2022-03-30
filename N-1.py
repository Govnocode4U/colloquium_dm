def COM_NN_D(n1, arr1, n2, arr2):
    if (n1 > n2):
        return 2
    elif (n1 < n2):
        return 1
    else:
        for i in range(0, n1):
            if (arr1[i] > arr2[2]):
                return 2
            elif (arr1[i] < arr2[i]):
                return 1
        return 0
