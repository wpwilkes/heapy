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

maxheap = heapy.MaxHeap()
minheap = heapy.MinHeap()
for i in range(10):
    maxheap.insert((i, None))
    minheap.insert((i, None))

[maxheap.remove()[0] for _ in range(10)]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

[minheap.remove()[0] for _ in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```