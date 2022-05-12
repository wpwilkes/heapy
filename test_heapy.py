"""
Test suite for heapy.
"""

import unittest

import heapy


class TestHeapy(unittest.TestCase):

    def test_MaxHeap(self):
        mheap = heapy.MaxHeap()
        for i in range(5):
            mheap.insert(i, None)
        self.assertTrue(mheap.remove()[0] == 4)
        self.assertTrue(mheap.remove()[0] == 3)

    def test_MinHeap(self):
        mheap = heapy.MinHeap()
        for i in range(5):
            mheap.insert(i, None)
        self.assertTrue(mheap.remove()[0] == 0)
        self.assertTrue(mheap.remove()[0] == 1)


if __name__ == "__main__":
    unittest.main()
