# Matrix Operations

Pymat provides operations for working with matrix structure and common matrix mathematics.

Let:

```python
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])
```

## Transpose

The `transpose` property exchanges the rows and columns of a matrix.

```python
T = A.transpose
```

Result:

```text
[[1, 3],
 [2, 4]]
```

For a matrix of order `m × n`, the transpose has order `n × m`.

### Usage

```python
A.transpose
```

---

## Minor

The `minor(rowIndex, colIndex)` method removes the specified row and column and returns the resulting matrix.

For:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])
```

```python
A.minor(0, 0)
```

Result:

```text
[[4]]
```

For a larger matrix:

```python
A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

A.minor(0, 1)
```

Result:

```text
[[4, 6],
 [7, 9]]
```

The row and column indices are zero-based.

### Signature

```python
A.minor(rowIndex, colIndex)
```

---

## Cofactor

The `cofactor(rowIndex, colIndex)` method calculates the cofactor of an element.

The cofactor is calculated as:

```text
Cᵢⱼ = (-1)⁽ⁱ⁺ʲ⁾ Mᵢⱼ
```

where `Mᵢⱼ` is the determinant of the corresponding minor.

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

A.cofactor(0, 0)
```

Result:

```text
4
```

The indices are zero-based.

### Signature

```python
A.cofactor(rowIndex, colIndex)
```

---

## Matrix of Minors

The `matrixOfMinors` property creates a matrix containing the determinant of the minor corresponding to every element.

For:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])
```

```python
A.matrixOfMinors
```

Result:

```text
[[4, 3],
 [2, 1]]
```

Each element represents the determinant of the corresponding minor.

### Usage

```python
A.matrixOfMinors
```

---

## Matrix of Cofactors

The `matrixOfCofactors` property creates a matrix containing the cofactor corresponding to every element.

For:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])
```

```python
A.matrixOfCofactors
```

Result:

```text
[[4, -3],
 [-2, 1]]
```

### Usage

```python
A.matrixOfCofactors
```

---

## Determinant

The `determinant` property calculates the determinant of a square matrix.

### 1 × 1 matrix

```python
A = Matrix([[5]])

A.determinant
```

Result:

```text
5
```

### 2 × 2 matrix

For:

```text
[a  b]
[c  d]
```

the determinant is:

```text
ad - bc
```

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

A.determinant
```

Result:

```text
-2
```

### Larger matrices

For matrices larger than `2 × 2`, Pymat calculates the determinant using cofactor expansion along the first row.

```python
A = Matrix([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

A.determinant
```

The matrix must be square. A `ValueError` is raised for a non-square matrix.

### Usage

```python
A.determinant
```

---

## Trace

The `trace` property returns the sum of the elements on the main diagonal.

For:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])
```

```python
A.trace
```

Result:

```text
5
```

because:

```text
1 + 4 = 5
```

The matrix must be square. A `ValueError` is raised for a non-square matrix.

### Usage

```python
A.trace
```

---

## Adjoint

The `adjoint` property returns the transpose of the matrix of cofactors.

Conceptually:

```text
adj(A) = transpose(matrixOfCofactors(A))
```

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

A.adjoint
```

Result:

```text
[[4, -2],
 [-3, 1]]
```

### Usage

```python
A.adjoint
```

---

## Inverse

The `inverse` property calculates the inverse of an invertible square matrix.

Pymat uses the relationship:

```text
A⁻¹ = adj(A) / det(A)
```

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

A.inverse
```

Result:

```text
[[-2.0, 1.0],
 [1.5, -0.5]]
```

An inverse exists only for an invertible matrix. If the matrix is not invertible, a `ValueError` is raised.

### Usage

```python
A.inverse
```

---

## Operations Summary

| Operation           | Syntax                | Result                                     |
| ------------------- | --------------------- | ------------------------------------------ |
| Transpose           | `A.transpose`         | Transposed matrix                          |
| Minor               | `A.minor(i, j)`       | Matrix with row `i` and column `j` removed |
| Cofactor            | `A.cofactor(i, j)`    | Cofactor value                             |
| Matrix of minors    | `A.matrixOfMinors`    | Matrix of minor determinants               |
| Matrix of cofactors | `A.matrixOfCofactors` | Matrix of cofactors                        |
| Determinant         | `A.determinant`       | Scalar determinant                         |
| Trace               | `A.trace`             | Sum of main diagonal                       |
| Adjoint             | `A.adjoint`           | Transpose of cofactor matrix               |
| Inverse             | `A.inverse`           | Inverse matrix                             |
