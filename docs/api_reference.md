# API Reference

This page provides a quick reference for the public `Matrix` API.

## Import

```python
from matrix import Matrix
```

---

# Matrix Construction

## `Matrix(m)`

Creates a matrix from a nested list.

```python
A = Matrix([
    [1, 2],
    [3, 4]
])
```

---

# Class Methods

## `Matrix.one(rows, cols=None)`

Creates a matrix containing only `1`.

```python
Matrix.one(2, 3)
```

## `Matrix.zero(rows, cols=None)`

Creates a matrix containing only `0`.

```python
Matrix.zero(2, 3)
```

## `Matrix.identity(n)`

Creates an `n × n` identity matrix.

```python
Matrix.identity(3)
```

## `Matrix.constant(rows, cols=None, value=0)`

Creates a matrix where every element has the specified value.

```python
Matrix.constant(2, 3, 7)
```

## `Matrix.diagonal(diag_list)`

Creates a diagonal matrix from a list of diagonal values.

```python
Matrix.diagonal([1, 2, 3])
```

## `Matrix.random(rows, cols=None, low=0, high=10)`

Creates a matrix containing randomly generated integers.

```python
Matrix.random(3, 4, 0, 10)
```

## `Matrix.elementwise(rows, cols=None, func=lambda i, j: 0)`

Creates a matrix by applying a function to every `(row, column)` position.

```python
Matrix.elementwise(
    2,
    3,
    lambda i, j: i + j
)
```

## `Matrix.from_string(my_string, dtype=float, row_sep='\n')`

Creates a matrix by parsing values from a string.

```python
Matrix.from_string(
    "1 2 3\n4 5 6",
    dtype=int
)
```

---

# Arithmetic Operators

| Syntax       | Operation                |
| ------------ | ------------------------ |
| `A + B`      | Element-wise addition    |
| `A - B`      | Element-wise subtraction |
| `A * B`      | Matrix multiplication    |
| `A * scalar` | Scalar multiplication    |
| `scalar * A` | Scalar multiplication    |
| `A / scalar` | Scalar division          |
| `-A`         | Matrix negation          |
| `A ** n`     | Matrix power             |

---

# Matrix Access

## `A[i, j]`

Returns an individual matrix element.

```python
value = A[0, 1]
```

## `A[i, j] = value`

Changes an individual matrix element.

```python
A[0, 1] = 10
```

## Iteration

A matrix can be iterated over row by row.

```python
for row in A:
    print(row)
```

---

# Matrix Information

## `A.order`

Returns the matrix dimensions as:

```text
(rows, columns)
```

Example:

```python
A.order
```

Result:

```text
(2, 3)
```

## `A.transpose`

Returns the transpose of the matrix.

## `A.traverse`

Returns the matrix elements in traversal order.

---

# Matrix Manipulation

## `A.insertRow(rowMat)`

Appends a row to the matrix.

## `A.insertCol(colMat)`

Appends a column to the matrix.

## `A.delRow(rowIndex, inplace=False)`

Deletes a row.

By default, returns a new matrix.

With `inplace=True`, modifies the existing matrix.

## `A.delCol(colIndex, inplace=False)`

Deletes a column.

By default, returns a new matrix.

With `inplace=True`, modifies the existing matrix.

## `A.getRow(rowIndex)`

Returns a row as a Python list.

## `A.getCol(colIndex)`

Returns a column as a Python list.

---

# Matrix Properties

| Property                | Description                                     |
| ----------------------- | ----------------------------------------------- |
| `A.isSqrMatrix`         | Checks whether the matrix is square             |
| `A.isDiagMatrix`        | Checks whether the matrix is diagonal           |
| `A.isColMatrix`         | Checks whether the matrix has one column        |
| `A.isRowMatrix`         | Checks whether the matrix has one row           |
| `A.isSclrMatrix`        | Checks whether the matrix is scalar             |
| `A.isIdntMatrix`        | Checks whether the matrix is an identity matrix |
| `A.isZeroMatrix`        | Checks whether every element is zero            |
| `A.isSymtMatrix`        | Checks whether the matrix is symmetric          |
| `A.isSkewSymtMatrix`    | Checks whether the matrix is skew-symmetric     |
| `A.isInvertible`        | Checks whether the matrix is invertible         |
| `A.isSingularMatrix`    | Checks whether the determinant is zero          |
| `A.isNonSingularMatrix` | Checks whether the determinant is non-zero      |

---

# Matrix Validation Methods

## `A.isValidIndex(index)`

Checks whether a supplied `(row, column)` index is valid.

Returns:

```text
True
```

or:

```text
False
```

## `A.isEqualOrder(other)`

Checks whether two matrices have the same dimensions.

## `A.isMultiplicable(other)`

Checks whether two matrices satisfy the dimension requirement for matrix multiplication.

---

# Matrix Operations

## `A.minor(rowIndex, colIndex)`

Returns the matrix obtained by removing the specified row and column.

## `A.cofactor(rowIndex, colIndex)`

Returns the cofactor of the specified element.

## `A.matrixOfMinors`

Returns the matrix of minor determinants.

## `A.matrixOfCofactors`

Returns the matrix of cofactors.

## `A.determinant`

Returns the determinant of a square matrix.

## `A.trace`

Returns the sum of the main diagonal.

## `A.adjoint`

Returns the adjoint of the matrix.

## `A.inverse`

Returns the inverse of an invertible matrix.

---

# Python Special Methods

Pymat implements Python special methods to provide natural operator behavior.

| Method        | Purpose                                  |
| ------------- | ---------------------------------------- |
| `__init__`    | Creates a matrix                         |
| `__repr__`    | Returns the representation of the matrix |
| `__str__`     | Returns the string representation        |
| `__eq__`      | Compares two matrices                    |
| `__add__`     | Matrix addition                          |
| `__sub__`     | Matrix subtraction                       |
| `__mul__`     | Matrix/scalar multiplication             |
| `__truediv__` | Scalar division                          |
| `__neg__`     | Matrix negation                          |
| `__rmul__`    | Right-side multiplication                |
| `__pow__`     | Matrix power                             |
| `__getitem__` | Matrix element access                    |
| `__setitem__` | Matrix element assignment                |
| `__iter__`    | Iterates through matrix rows             |

---

# Complete API Overview

```text
Matrix
│
├── Construction
│   ├── Matrix()
│   ├── one()
│   ├── zero()
│   ├── identity()
│   ├── constant()
│   ├── diagonal()
│   ├── random()
│   ├── elementwise()
│   └── from_string()
│
├── Arithmetic
│   ├── +
│   ├── -
│   ├── *
│   ├── /
│   ├── -
│   └── **
│
├── Access & Manipulation
│   ├── [i, j]
│   ├── insertRow()
│   ├── insertCol()
│   ├── delRow()
│   ├── delCol()
│   ├── getRow()
│   └── getCol()
│
├── Properties
│   ├── order
│   ├── transpose
│   ├── traverse
│   ├── isSqrMatrix
│   ├── isDiagMatrix
│   ├── isColMatrix
│   ├── isRowMatrix
│   ├── isSclrMatrix
│   ├── isIdntMatrix
│   ├── isZeroMatrix
│   ├── isSymtMatrix
│   ├── isSkewSymtMatrix
│   ├── isInvertible
│   ├── isSingularMatrix
│   └── isNonSingularMatrix
│
└── Operations
    ├── minor()
    ├── cofactor()
    ├── matrixOfMinors
    ├── matrixOfCofactors
    ├── determinant
    ├── trace
    ├── adjoint
    └── inverse
```
