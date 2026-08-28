# Constructors

Pymat provides several class methods for creating matrices without manually writing the complete nested list.

All constructors are available through the `Matrix` class.

## `Matrix(rows, cols=None)`

The main constructor creates a matrix from a nested list.

```python
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])
```

---

## `Matrix.one(rows, cols=None)`

Creates a matrix containing only `1`.

If `cols` is omitted, a square matrix is created.

### Square matrix

```python
A = Matrix.one(3)
```

Result:

```text
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
```

### Rectangular matrix

```python
A = Matrix.one(2, 4)
```

Result:

```text
[[1, 1, 1, 1],
 [1, 1, 1, 1]]
```

### Signature

```python
Matrix.one(rows, cols=None)
```

---

## `Matrix.zero(rows, cols=None)`

Creates a matrix containing only `0`.

If `cols` is omitted, a square matrix is created.

```python
A = Matrix.zero(2, 3)
```

Result:

```text
[[0, 0, 0],
 [0, 0, 0]]
```

### Signature

```python
Matrix.zero(rows, cols=None)
```

---

## `Matrix.identity(n)`

Creates an `n × n` identity matrix.

```python
A = Matrix.identity(3)
```

Result:

```text
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
```

### Signature

```python
Matrix.identity(n)
```

---

## `Matrix.constant(rows, cols=None, value=0)`

Creates a matrix where every element has the specified value.

```python
A = Matrix.constant(2, 3, 7)
```

Result:

```text
[[7, 7, 7],
 [7, 7, 7]]
```

If `value` is omitted, the default value is `0`.

```python
A = Matrix.constant(2)
```

Result:

```text
[[0, 0],
 [0, 0]]
```

### Signature

```python
Matrix.constant(rows, cols=None, value=0)
```

---

## `Matrix.diagonal(diag_list)`

Creates a square diagonal matrix using the values provided in `diag_list`.

```python
A = Matrix.diagonal([1, 2, 3])
```

Result:

```text
[[1, 0, 0],
 [0, 2, 0],
 [0, 0, 3]]
```

### Signature

```python
Matrix.diagonal(diag_list)
```

---

## `Matrix.random(rows, cols=None, low=0, high=10)`

Creates a matrix containing randomly generated integers.

The values are generated between `low` and `high`.

```python
A = Matrix.random(2, 3, 1, 5)
```

A possible result is:

```text
[[3, 1, 5],
 [2, 4, 1]]
```

Because the values are random, the result can differ each time.

If `cols` is omitted, a square matrix is created.

```python
A = Matrix.random(3)
```

### Signature

```python
Matrix.random(rows, cols=None, low=0, high=10)
```

---

## `Matrix.elementwise(rows, cols=None, func=lambda i, j: 0)`

Creates a matrix by calling a function for every matrix position.

The function receives the row index `i` and column index `j`.

```python
A = Matrix.elementwise(
    2,
    3,
    lambda i, j: i + j
)
```

Result:

```text
[[0, 1, 2],
 [1, 2, 3]]
```

The indices are zero-based.

For example:

```text
A[0, 0] → func(0, 0)
A[0, 1] → func(0, 1)
A[1, 0] → func(1, 0)
```

### Signature

```python
Matrix.elementwise(
    rows,
    cols=None,
    func=lambda i, j: 0
)
```

---

## `Matrix.from_string(my_string, dtype=float, row_sep='\n')`

Creates a matrix by parsing numeric values from a string.

By default, rows are separated by newline characters and values within a row are separated by whitespace.

```python
from matrix import Matrix

A = Matrix.from_string("""
1 2 3
4 5 6
""")
```

Result:

```text
[[1.0, 2.0, 3.0],
 [4.0, 5.0, 6.0]]
```

The default `dtype` is `float`.

### Using another data type

The `dtype` argument controls how each value is converted.

```python
A = Matrix.from_string(
    "1 2 3\n4 5 6",
    dtype=int
)
```

Result:

```text
[[1, 2, 3],
 [4, 5, 6]]
```

### Custom row separator

The `row_sep` argument controls how rows are separated.

```python
A = Matrix.from_string(
    "1 2;3 4",
    dtype=int,
    row_sep=';'
)
```

Result:

```text
[[1, 2],
 [3, 4]]
```

### Signature

```python
Matrix.from_string(
    my_string,
    dtype=float,
    row_sep='\n'
)
```

### Parsing behavior

Before conversion, the implementation filters the input string and keeps:

* Digits
* Spaces
* `.`
* `+`
* `-`
* `j`
* The specified row separator

The resulting values are split into rows using `row_sep` and into individual values using whitespace.
