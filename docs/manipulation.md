# Matrix Manipulation

Pymat provides methods for inserting, deleting, and retrieving rows and columns.

Let:

```python
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])
```

## Insert a Row

`insertRow(rowMat)` adds a new row to the end of the matrix.

The length of `rowMat` must match the current number of columns.

```python
A.insertRow([5, 6])
```

Result:

```text
[[1, 2],
 [3, 4],
 [5, 6]]
```

If the row length does not match the number of columns, a `ValueError` is raised.

### Signature

```python
A.insertRow(rowMat)
```

---

## Insert a Column

`insertCol(colMat)` adds a new column to the end of the matrix.

The length of `colMat` must match the current number of rows.

```python
A.insertCol([5, 6])
```

Result:

```text
[[1, 2, 5],
 [3, 4, 6]]
```

If the column length does not match the number of rows, a `ValueError` is raised.

### Signature

```python
A.insertCol(colMat)
```

---

## Delete a Row

`delRow(rowIndex, inplace=False)` removes the specified row.

By default, it returns a **new matrix** and does not modify the original matrix.

```python
A = Matrix([
    [1, 2],
    [3, 4],
    [5, 6]
])

B = A.delRow(1)
```

`B` becomes:

```text
[[1, 2],
 [5, 6]]
```

while `A` remains unchanged.

### In-place deletion

Set `inplace=True` to modify the existing matrix:

```python
A.delRow(1, inplace=True)
```

The original matrix is modified.

### Signature

```python
A.delRow(rowIndex, inplace=False)
```

The row index is zero-based.

An invalid index raises `ValueError`.

---

## Delete a Column

`delCol(colIndex, inplace=False)` removes the specified column.

By default, it returns a **new matrix**.

```python
A = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])

B = A.delCol(1)
```

Result:

```text
[[1, 3],
 [4, 6]]
```

The original matrix remains unchanged.

### In-place deletion

Set `inplace=True` to modify the existing matrix:

```python
A.delCol(1, inplace=True)
```

### Signature

```python
A.delCol(colIndex, inplace=False)
```

The column index is zero-based.

An invalid index raises `ValueError`.

---

## Get a Row

`getRow(rowIndex)` returns the specified row as a Python list.

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

row = A.getRow(1)
```

Result:

```python
[3, 4]
```

The row index is zero-based.

An invalid index raises `ValueError`.

### Signature

```python
A.getRow(rowIndex)
```

---

## Get a Column

`getCol(colIndex)` returns the specified column as a Python list.

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

column = A.getCol(0)
```

Result:

```python
[1, 3]
```

The column index is zero-based.

An invalid index raises `ValueError`.

### Signature

```python
A.getCol(colIndex)
```

---

## Indexing

Individual matrix elements can be accessed using two-dimensional indexing.

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

value = A[0, 1]
```

Result:

```text
2
```

Indices are zero-based.

Values can also be changed using indexing:

```python
A[0, 1] = 10
```

The matrix becomes:

```text
[[1, 10],
 [3, 4]]
```

---

## Iteration

A `Matrix` can be iterated over directly.

```python
for row in A:
    print(row)
```

Each iteration produces a row of the matrix as a Python list.

For example:

```text
[1, 2]
[3, 4]
```

---

## Manipulation Summary

| Operation              | Syntax                      | Result                            |
| ---------------------- | --------------------------- | --------------------------------- |
| Insert row             | `A.insertRow(row)`          | Adds row to the matrix            |
| Insert column          | `A.insertCol(col)`          | Adds column to the matrix         |
| Delete row             | `A.delRow(i)`               | Returns matrix without row `i`    |
| Delete row in place    | `A.delRow(i, inplace=True)` | Modifies `A`                      |
| Delete column          | `A.delCol(j)`               | Returns matrix without column `j` |
| Delete column in place | `A.delCol(j, inplace=True)` | Modifies `A`                      |
| Get row                | `A.getRow(i)`               | Returns row as a list             |
| Get column             | `A.getCol(j)`               | Returns column as a list          |
| Get element            | `A[i, j]`                   | Returns an element                |
| Set element            | `A[i, j] = value`           | Changes an element                |
| Iterate                | `for row in A`              | Iterates over rows                |
