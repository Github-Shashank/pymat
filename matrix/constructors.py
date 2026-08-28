import random


def one(matrix_class, rows, cols=None):
    if cols is None:
        cols = rows

    return matrix_class([
        [1 for _ in range(cols)]
        for _ in range(rows)
    ])


def zero(matrix_class, rows, cols=None):
    if cols is None:
        cols = rows

    return matrix_class([
        [0 for _ in range(cols)]
        for _ in range(rows)
    ])


def identity(matrix_class, n):
    return matrix_class([
        [1 if i == j else 0 for j in range(n)]
        for i in range(n)
    ])


def constant(matrix_class, rows, cols=None, value=0):
    if cols is None:
        cols = rows

    return matrix_class([
        [value for _ in range(cols)]
        for _ in range(rows)
    ])

def diagonal(matrix_class, diag_list):
    n = len(diag_list)

    return matrix_class([
        [diag_list[i] if i == j else 0 for j in range(n)]
        for i in range(n)
    ])

def random_matrix(matrix_class, rows, cols=None, low=0, high=10):
    if cols is None:
        cols = rows

    return matrix_class([
        [random.randint(low, high) for _ in range(cols)]
        for _ in range(rows)
    ])

def elementwise(matrix_class, rows, cols=None, func=lambda i, j: 0):
    if cols is None:
        cols = rows

    return matrix_class([
        [func(i, j) for j in range(cols)]
        for i in range(rows)
    ])

def from_string(
    matrix_class,
    my_string,
    dtype=float,
    row_sep='\n'
):
    s = my_string.strip()

    char_list = [
        char
        for char in s
        if char.isdigit() or char in ' .+-j' + row_sep
    ]

    clean_string = "".join(char_list)

    matrix_data = [
        [
            dtype(value)
            for value in row.split()
            if value
        ]
        for row in clean_string.split(row_sep)
        if row.strip()
    ]

    return matrix_class(matrix_data)