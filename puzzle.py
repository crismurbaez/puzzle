def matrix_multi(a, b, mod):
    """Multiplicador de dos matrices de dimensiones de 3x3.
    Se obtiene el módulo 'mod' para tener
    como resultado solamente a los últimos dígitos
    """
    result_multi = [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0] + a[0][2] * b[2][0]) % mod,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1] + a[0][2] * b[2][1]) % mod,
            (a[0][0] * b[0][2] + a[0][1] * b[1][2] + a[0][2] * b[2][2]) % mod,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0] + a[1][2] * b[2][0]) % mod,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1] + a[1][2] * b[2][1]) % mod,
            (a[1][0] * b[0][2] + a[1][1] * b[1][2] + a[1][2] * b[2][2]) % mod,
        ],
        [
            (a[2][0] * b[0][0] + a[2][1] * b[1][0] + a[2][2] * b[2][0]) % mod,
            (a[2][0] * b[0][1] + a[2][1] * b[1][1] + a[2][2] * b[2][1]) % mod,
            (a[2][0] * b[0][2] + a[2][1] * b[1][2] + a[2][2] * b[2][2]) % mod,
        ],
    ]
    return result_multi


def power_matrix(matrix, exp, mod):
    """Se eleva una matriz a la potencia de 'exp'.
    Se utiliza el método de exponenciación binaria
    que permite realizar potencias con exponentes muy grandes
    """
    result = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Matriz identidad inicial
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_multi(result, matrix, mod)
        matrix = matrix_multi(matrix, matrix, mod)
        exp //= 2
    return result


def tribonacci(orden, digit):
    """
    Se calcula el n-ésimo término de la secuencia de Tribonacci.
    """
    mod = 10**digit
    if orden == 0:
        return 2023
    elif orden == 1:
        return 2024
    elif orden == 2:
        return 2025
    """ 
    Matriz de transformación que se obtiene al observar
    la relación de recurrencia que define la secuencia de Tribonacci.
    """
    matrix_transf = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    matrix_result = power_matrix(matrix_transf, orden - 3, mod)
    result = (
        2025 * matrix_result[0][0]
        + 2024 * matrix_result[0][1]
        + 2023 * matrix_result[0][2]
    ) % mod

    return result


# Se calcula el Tribonacci
orden = 2023202320232023
digit = 4
resultado = tribonacci(orden, digit)
print(
    f"Los últimos {digit} dígitos del orden {orden} de la secuencia de Tribonacci son: {resultado}"
)
