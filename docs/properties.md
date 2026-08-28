# Matrix Properties

Pymat provides properties for identifying common types and mathematical characteristics of matrices.

Let:

```python
from matrix import Matrix
```

## `isSqrMatrix`

Returns `True` if the matrix has the same number of rows and columns.

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

A.isSqrMatrix
```

Result:

```text
True
```

A `2 × 3` matrix is not square:

```python
A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])

A.isSqrMatrix
```

Result:

```text
False
```

---

## `isDiagMatrix`

Returns `True` if the matrix is square and every element outside the main diagonal is `0`.

```python
A = Matrix([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
])

A.isDiagMatrix
```

Result:

```text
True
```

A matrix with a non-zero off-diagonal element is not diagonal.

---

## `isColMatrix`

Returns `True` if the matrix has exactly one column.

```python
A = Matrix([
    [1],
    [2],
    [3]
])

A.isColMatrix
```

Result:

```text
True
```

---

## `isRowMatrix`

Returns `True` if the matrix has exactly one row.

```python
A = Matrix([
    [1, 2, 3]
])

A.isRowMatrix
```

Result:

```text
True
```

---

## `isSclrMatrix`

Returns `True` if the matrix is diagonal and all diagonal elements have the same value.

```python
A = Matrix([
    [5, 0, 0],
    [0, 5, 0],
    [0, 0, 5]
])

A.isSclrMatrix
```

Result:

```text
True
```

The matrix must first satisfy the diagonal matrix condition.

---

## `isIdntMatrix`

Returns `True` if the matrix is diagonal and every diagonal element is `1`.

```python
A = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

A.isIdntMatrix
```

Result:

```text
True
```

---

## `isZeroMatrix`

Returns `True` if every element of the matrix is `0`.

```python
A = Matrix([
    [0, 0],
    [0, 0]
])

A.isZeroMatrix
```

Result:

```text
True
```

---

## `isSymtMatrix`

Returns `True` if the matrix is equal to its transpose.

The condition is:

```text
A = Aᵀ
```

Example:

```python
A = Matrix([
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
])

A.isSymtMatrix
```

Result:

```text
True
```

---

## `isSkewSymtMatrix`

Returns `True` if the negative of the matrix is equal to its transpose.

The condition is:

```text
-A = Aᵀ
```

Pymat checks this using:

```python
-1 * A == A.transpose
```

Example:

```python
A = Matrix([
    [0, 2],
    [-2, 0]
])

A.isSkewSymtMatrix
```

Result:

```text
True
```

---

## `isInvertible`

Returns `True` when the matrix is square and its determinant is not zero.

The condition is:

```text
A is square
and
det(A) ≠ 0
```

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

A.isInvertible
```

Result:

```text
True
```

A non-square matrix is not considered invertible by this property.

---

## `isSingularMatrix`

Returns `True` when the determinant is zero.

The condition is:

```text
det(A) = 0
```

Example:

```python
A = Matrix([
    [1, 2],
    [2, 4]
])

A.isSingularMatrix
```

Result:

```text
True
```

---

## `isNonSingularMatrix`

Returns `True` when the determinant is not zero.

The condition is:

```text
det(A) ≠ 0
```

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

A.isNonSingularMatrix
```

Result:

```text
True
```

---

## Property Summary

| Property              | Condition                                               |
| --------------------- | ------------------------------------------------------- |
| `isSqrMatrix`         | Number of rows equals number of columns                 |
| `isDiagMatrix`        | Square matrix with zero off-diagonal elements           |
| `isColMatrix`         | Exactly one column                                      |
| `isRowMatrix`         | Exactly one row                                         |
| `isSclrMatrix`        | Diagonal matrix with equal diagonal elements            |
| `isIdntMatrix`        | Diagonal matrix with all diagonal elements equal to `1` |
| `isZeroMatrix`        | Every element is `0`                                    |
| `isSymtMatrix`        | `A == Aᵀ`                                               |
| `isSkewSymtMatrix`    | `-A == Aᵀ`                                              |
| `isInvertible`        | Square matrix with non-zero determinant                 |
| `isSingularMatrix`    | Determinant equals `0`                                  |
| `isNonSingularMatrix` | Determinant is not `0`                                  |
