import unittest
from matrix import Matrix
from matrix.validators import (
    check_matrix,
    is_equal_order,
    is_valid_index,
    is_multiplicable
)


class TestMatrix(unittest.TestCase):

    def test_check_matrix_valid(self):
        m = [[1, 2], [3, 4]]

        self.assertEqual(check_matrix(m), True)

    def test_check_matrix_invalid(self):
        m = [[1, 2], [3]]

        self.assertEqual(check_matrix(m), [3])

    def test_is_equal_order_true(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[5, 6], [7, 8]])

        self.assertTrue(is_equal_order(A, B))

    def test_is_equal_order_false(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[1, 2, 3], [4, 5, 6]])

        self.assertFalse(is_equal_order(A, B))

    def test_is_valid_index_true(self):
        A = Matrix([[1, 2], [3, 4]])

        self.assertTrue(is_valid_index(A, (0, 0)))
        self.assertTrue(is_valid_index(A, (1, 1)))

    def test_is_valid_index_false(self):
        A = Matrix([[1, 2], [3, 4]])

        self.assertFalse(is_valid_index(A, (2, 0)))
        self.assertFalse(is_valid_index(A, (0, 2)))
        self.assertFalse(is_valid_index(A, (1,)))
        self.assertFalse(is_valid_index(A, (0, 1, 2)))

    def test_is_multiplicable_true(self):
        A = Matrix([[1, 2, 3], [4, 5, 6]])
        B = Matrix([[1, 2], [3, 4], [5, 6]])

        self.assertTrue(is_multiplicable(A, B))

    def test_is_multiplicable_false(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[1, 2], [3, 4], [5, 6]])

        self.assertFalse(is_multiplicable(A, B))

    def test_transpose(self):
        A = Matrix([
            [1, 2, 3],
            [4, 5, 6]
        ])

        expected = Matrix([
            [1, 4],
            [2, 5],
            [3, 6]
        ])

        self.assertEqual(A.transpose, expected)

    def test_minor(self):
        A = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        self.assertEqual(
            A.minor(0, 0),
            Matrix([
                [5, 6],
                [8, 9]
            ])
        )


    def test_cofactor(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(A.cofactor(0, 0), 4)
        self.assertEqual(A.cofactor(0, 1), -3)


    def test_determinant(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(A.determinant, -2)


    def test_determinant_3x3(self):
        A = Matrix([
            [1, 2, 3],
            [0, 1, 4],
            [5, 6, 0]
        ])

        self.assertEqual(A.determinant, 1)

        def test_matrix_of_minors(self):
            A = Matrix([
                [1, 2],
                [3, 4]
            ])

            result = A.matrixOfMinors

            self.assertEqual(result[0, 0], 4)
            self.assertEqual(result[0, 1], 3)
            self.assertEqual(result[1, 0], 2)
            self.assertEqual(result[1, 1], 1)   

    def test_matrix_of_cofactors(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        result = A.matrixOfCofactors

        self.assertEqual(result[0, 0], 4)
        self.assertEqual(result[0, 1], -3)
        self.assertEqual(result[1, 0], -2)
        self.assertEqual(result[1, 1], 1)

    def test_adjoint(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        expected = Matrix([
            [4, -2],
            [-3, 1]
        ])

        self.assertEqual(A.adjoint, expected)

    def test_inverse(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        expected = Matrix([
            [-2, 1],
            [1.5, -0.5]
        ])

        self.assertEqual(A.inverse, expected)

    def test_inverse_singular(self):
        A = Matrix([
            [1, 2],
            [2, 4]
        ])

        with self.assertRaises(ValueError):
            A.inverse

    def test_one(self):
        self.assertEqual(
            Matrix.one(2, 3),
            Matrix([
                [1, 1, 1],
                [1, 1, 1]
            ])
        )

    def test_zero(self):
        self.assertEqual(
            Matrix.zero(2, 3),
            Matrix([
                [0, 0, 0],
                [0, 0, 0]
            ])
        )

    def test_identity(self):
        self.assertEqual(
            Matrix.identity(3),
            Matrix([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ])
        )

    def test_constant(self):
        self.assertEqual(
            Matrix.constant(2, 3, 7),
            Matrix([
                [7, 7, 7],
                [7, 7, 7]
            ])
        )

    def test_diagonal(self):
        self.assertEqual(
            Matrix.diagonal([1, 2, 3]),
            Matrix([
                [1, 0, 0],
                [0, 2, 0],
                [0, 0, 3]
            ])
        )

    def test_elementwise(self):
        result = Matrix.elementwise(
            2,
            3,
            lambda i, j: i + j
        )

        self.assertEqual(
            result,
            Matrix([
                [0, 1, 2],
                [1, 2, 3]
            ])
        )

    def test_random(self):
        result = Matrix.random(3, 4, 1, 5)

        self.assertEqual(result.order, (3, 4))

        for value in result.traverse:
            self.assertTrue(1 <= value <= 5)

    def test_from_string(self):
        result = Matrix.from_string(
            "1 2 3\n4 5 6",
            dtype=int
        )

        self.assertEqual(
            result,
            Matrix([
                [1, 2, 3],
                [4, 5, 6]
            ])
        )


    def test_divide_scalar(self):
        A = Matrix([
            [2, 4],
            [6, 8]
        ])

        self.assertEqual(
            A / 2,
            Matrix([
                [1, 2],
                [3, 4]
            ])
        )


    def test_divide_by_zero(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        with self.assertRaises(ZeroDivisionError):
            A / 0

    def test_negate(self):
        A = Matrix([
            [1, -2],
            [-3, 4]
        ])

        self.assertEqual(
            -A,
            Matrix([
                [-1, 2],
                [3, -4]
            ])
        )

    def test_power(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(
            A ** 2,
            Matrix([
                [7, 10],
                [15, 22]
            ])
        )

    def test_right_multiply(self):
        A = Matrix([
            [1, 2],
            [3, 4]
        ])

        self.assertEqual(
            3 * A,
            Matrix([
                [3, 6],
                [9, 12]
            ])
        )


if __name__ == "__main__":
    unittest.main()