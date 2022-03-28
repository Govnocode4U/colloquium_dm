def older_polynomial_coefficient(polynom):
    coefficient = max(*dict.keys(polynom))
    return polynom[coefficient]