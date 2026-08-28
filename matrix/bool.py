def is_square(matrix):
    rows, cols = matrix.order
    return rows == cols


def is_diagonal(matrix):
    if not is_square(matrix):
        return False

    rows, cols = matrix.order

    values = {
        matrix.m[i][j]
        for i in range(rows)
        for j in range(cols)
        if i != j
    }

    return values == {0}


def is_column(matrix):
    return matrix.order[1] == 1


def is_row(matrix):
    return matrix.order[0] == 1


def is_scalar(matrix):
    if not is_diagonal(matrix):
        return False

    rows, cols = matrix.order

    values = {
        matrix.m[i][j]
        for i in range(rows)
        for j in range(cols)
        if i == j
    }

    return len(values) == 1


def is_identity(matrix):
    if not is_diagonal(matrix):
        return False

    rows, cols = matrix.order

    values = {
        matrix.m[i][j]
        for i in range(rows)
        for j in range(cols)
        if i == j
    }

    return values == {1}


def is_zero(matrix):
    rows, cols = matrix.order

    values = {
        matrix.m[i][j]
        for i in range(rows)
        for j in range(cols)
    }

    return values == {0}


def is_symmetric(matrix):
    return matrix == matrix.transpose


def is_skew_symmetric(matrix):
    return -1 * matrix == matrix.transpose


def is_invertible(matrix):
    return matrix.isSqrMatrix and matrix.determinant != 0


def is_singular(matrix):
    return matrix.determinant == 0


def is_non_singular(matrix):
    return matrix.determinant != 0