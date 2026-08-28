# Arithmetic

Pymat supports arithmetic operations through Python's operator overloading.

Let:

```python
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])
```

## Addition

The `+` operator performs element-wise matrix addition.

```python
C = A + B
```

Result:

```text
[[6, 8],
 [10, 12]]
```

Both matrices must have the same order.

```python
A + B
```

If their dimensions are different, a `ValueError` is raised.

---

## Subtraction

The `-` operator performs element-wise matrix subtraction.

```python
C = A - B
```

Result:

```text
[[-4, -4],
 [-4, -4]]
```

Both matrices must have the same order.

If their dimensions are different, a `ValueError` is raised.

---

## Multiplication

The `*` operator supports both scalar multiplication and matrix multiplication.

### Scalar multiplication

A matrix can be multiplied by an integer, floating-point number, or complex number.

```python
C = A * 2
```

Result:

```text
[[2, 4],
 [6, 8]]
```

Complex values are also supported:

```python
C = A * (2 + 3j)
```

### Matrix multiplication

Two matrices can be multiplied when their dimensions are compatible.

For:

```text
A: m × n
B: n × p
```

the result is:

```text
m × p
```

Example:

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])

C = A * B
```

Result:

```text
[[19, 22],
 [43, 50]]
```

If the matrices cannot be multiplied, a `ValueError` is raised.

---

## Right Scalar Multiplication

Pymat supports scalar multiplication from the left through `__rmul__`.

```python
C = 2 * A
```

Result:

```text
[[2, 4],
 [6, 8]]
```

---

## Division

The `/` operator performs element-wise division of every matrix element by a scalar.

```python
C = A / 2
```

Result:

```text
[[0.5, 1.0],
 [1.5, 2.0]]
```

Division by zero raises `ZeroDivisionError`.

```python
A / 0
```

---

## Negation

The unary `-` operator negates every element of the matrix.

```python
C = -A
```

Result:

```text
[[-1, -2],
 [-3, -4]]
```

---

## Power

The `**` operator raises a matrix to a positive integer power.

```python
A = Matrix([
    [1, 2],
    [3, 4]
])

C = A ** 2
```

Result:

```text
[[7, 10],
 [15, 22]]
```

The implementation starts with an identity matrix and repeatedly multiplies it by the original matrix.

### Supported exponent

The current implementation accepts a positive integer exponent:

```python
A ** 1
A ** 2
A ** 3
```

The current implementation does not provide a result for zero or negative exponents.

---

## Operator Summary

| Operator     | Operation                | Supported operands   |
| ------------ | ------------------------ | -------------------- |
| `A + B`      | Element-wise addition    | Matrix + Matrix      |
| `A - B`      | Element-wise subtraction | Matrix - Matrix      |
| `A * B`      | Matrix multiplication    | Matrix × Matrix      |
| `A * scalar` | Scalar multiplication    | Matrix × number      |
| `scalar * A` | Scalar multiplication    | Number × Matrix      |
| `A / scalar` | Scalar division          | Matrix ÷ number      |
| `-A`         | Element-wise negation    | Matrix               |
| `A ** n`     | Matrix power             | Positive integer `n` |
