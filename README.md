# Pymat

A modular Python library for matrix creation and manipulation.

## Installation

Clone the repository and install it:

```bash
git clone https://github.com/Github-Shashank/pymat.git
cd pymat
pip install -e .
```

## Usage

```python
from matrix import Matrix

A = Matrix([
    [1, 2],
    [3, 4]
])

print(A)
print(A.determinant)
```

## Features

* Matrix arithmetic
* Matrix multiplication
* Transpose
* Determinant
* Minors and cofactors
* Adjoint and inverse
* Matrix constructors
* Row and column manipulation
* Matrix validation
* Matrix property checks

## Testing

Run the test suite with:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Project Structure

```text
pymat/
├── matrix/
│   ├── arithmetic.py
│   ├── bool.py
│   ├── constructors.py
│   ├── exceptions.py
│   ├── manipulation.py
│   ├── matrix.py
│   ├── operations.py
│   └── validators.py
├── tests/
│   └── test_matrix.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## License

This project is licensed under the MIT License.
