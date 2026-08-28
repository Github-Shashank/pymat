def add(matrix, other):
    if not matrix.isEqualOrder(other):
        raise ValueError()

    rows, cols = matrix.order

    result = [
        [
            matrix.m[i][j] + other.m[i][j]
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def subtract(matrix, other):
    if not matrix.isEqualOrder(other):
        raise ValueError()

    rows, cols = matrix.order

    result = [
        [
            matrix.m[i][j] - other.m[i][j]
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def multiply(matrix, other):
    # Scalar multiplication
    if isinstance(other, (int, float, complex)):
        return type(matrix)(
            [
                [matrix.m[i][j] * other for j in range(matrix.order[1])]
                for i in range(matrix.order[0])
            ]
        )

    if not matrix.isMultiplicable(other):
        raise ValueError()

    rows = matrix.order[0]
    cols = other.order[1]

    result = [
        [
            sum(
                matrix.m[i][k] * other.m[k][j]
                for k in range(matrix.order[1])
            )
            for j in range(cols)
        ]
        for i in range(rows)
    ]

    return type(matrix)(result)


def divide(matrix, other):
    if other == 0:
        raise ZeroDivisionError("division by zero")

    return type(matrix)(
        [
            [matrix.m[i][j] / other for j in range(matrix.order[1])]
            for i in range(matrix.order[0])
        ]
    )


def negate(matrix):
    return type(matrix)(
        [
            [-matrix.m[i][j] for j in range(matrix.order[1])]
            for i in range(matrix.order[0])
        ]
    )


def power(matrix, raised_to):
    if isinstance(raised_to, int) and raised_to > 0:
        I = type(matrix).identity(matrix.order[0])

        for _ in range(raised_to):
            I = I * matrix

        return I
