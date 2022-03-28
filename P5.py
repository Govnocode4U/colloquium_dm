polynom = {1:5, 2:78, 4:128}
def older_polynomial_coefficient(polynom):
    coefficient = max(*dict.keys(polynom))
    return polynom[coefficient]
print(older_polynomial_coefficient(polynom))