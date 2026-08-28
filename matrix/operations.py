def transpose(matrix):
    rows, cols = matrix.order

    result = [
        [matrix.m[j][i] for j in range(rows)]
        for i in range(cols)
    ]

    return type(matrix)(result)


def minor(matrix, row_index, col_index):
    return matrix.delRow(row_index).delCol(col_index)


def cofactor(matrix, row_index, col_index):
    return ((-1) ** (row_index + col_index)) * determinant(
        minor(matrix, row_index, col_index)
    )


def determinant(matrix):
    rows, cols = matrix.order

    if rows != cols:
        raise ValueError()

    if rows == 1:
        return matrix.m[0][0]

    if rows == 2:
        m = matrix.m
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    return sum(
        matrix.m[0][i] * cofactor(matrix, 0, i)
        for i in range(cols)
    )


def matrix_of_minors(matrix):
    rows, cols = matrix.order

    result = [
        [
            determinant(minor(matrix, i, j))
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def matrix_of_cofactors(matrix):
    rows, cols = matrix.order

    result = [
        [
            cofactor(matrix, i, j)
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def trace(self):
    r,c = self.order
    if not r == c:
        raise ValueError()
    return sum(self.m[i][i] for i in range(r))


def adjoint(matrix):
    return matrix_of_cofactors(matrix).transpose


def inverse(matrix):
    if not matrix.isInvertible:
        raise ValueError()

    return adjoint(matrix) * (1 / determinant(matrix))