# heapy

![CI](https://github.com/wpwilkes/heapy/actions/workflows/python-package.yml/badge.svg?branch=develop)

Binary Heaps

## Installation

Clone the repository using https://github.com/wpwilkes/heapy.git.
Use `pip` to run the installation process.

```bash
pip install path/to/heapy/
```

## Test

After installing the package, be sure to run the tests to ensure the
software works as intended.

```bash
pytest path/to/tests/
```

## Usage

```python
import heapy

mheap = heapy.MinHeap()
for i in range(10):
    mheap.insert(i, i**2)
mheap.remove()
# (0, 0)
```