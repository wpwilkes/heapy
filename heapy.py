"""
Implementation of basic binary heaps.
"""

from typing import Any, Optional


KVPair = tuple[int, Any]


class MaxHeap:
    """
    Implementation of a max binary heap.
    """

    def __init__(self):
        """
        Instantiate the max binary heap.
        """
        self._array: list[KVPair] = []

    def insert(self, kvpair: KVPair) -> None:
        """
        Insert a given key-value pair into the heap.

        Parameters
        ----------
        kvpair : tuple[int, Any]
            The key-value pair to add to the heap.
        """
        self._array.append(kvpair)
        self._bubble_up()

    def _bubble_up(self):
        """
        Restore the heap-order property if necessary.
        """
        last_idx = len(self._array) - 1
        parent_idx = (last_idx) // 2
        while self._array[parent_idx][0] < self._array[last_idx][0]:
            self._array[parent_idx], self._array[last_idx] = self._array[last_idx], self._array[parent_idx]
            last_idx = parent_idx
            parent_idx = (parent_idx) // 2

    def remove(self) -> Optional[KVPair]:
        """
        Remove and return the key-value pair with the maximum key.

        Returns
        -------
        tuple[int, Any] :
            The key-value pair with the maximum key (if any).
        """
        if self._array:
            max_pair = self._array[0]
            self._array[0] = self._array[-1]
            self._array.pop()
            self._bubble_down(0)
            return max_pair

    def _bubble_down(self, idx: int) -> None:
        """
        Restore the heap-order property if necessary.
        """
        largest = idx
        l = 2 * idx + 1
        r = 2 * idx + 2
        n = len(self._array)
        if l < n:
            if self._array[idx][0] < self._array[l][0]:
                largest = l
        if r < n:
            if self._array[largest][0] < self._array[r][0]:
                largest = r
        if largest != idx:
            self._array[idx], self._array[largest] = self._array[largest], self._array[idx]
            self._bubble_down(largest)


class MinHeap:
    """
    Implementation of a min binary heap.
    """

    def __init__(self):
        """
        Instantiate the min binary heap.
        """
        self._array: list[KVPair] = []

    def insert(self, kvpair: KVPair) -> None:
        """
        Insert a given key-value pair into the heap.

        Parameters
        ----------
        kvpair : tuple[int, Any]
            The key-value pair to add to the heap.
        """
        self._array.append(kvpair)
        self._bubble_up()

    def _bubble_up(self):
        """
        Restore the heap-order property if necessary.
        """
        last_idx = len(self._array) - 1
        parent_idx = last_idx // 2
        while self._array[parent_idx][0] > self._array[last_idx][0]:
            self._array[parent_idx], self._array[last_idx] = self._array[last_idx], self._array[parent_idx]
            last_idx = parent_idx
            parent_idx = parent_idx // 2

    def remove(self) -> Optional[KVPair]:
        """
        Remove and return the key-value pair with the minimum key.

        Returns
        -------
        tuple[int, Any] :
            The key-value pair with the minimum key (if any).
        """
        if self._array:
            min_pair = self._array[0]
            self._array[0] = self._array[-1]
            self._array.pop()
            self._bubble_down(0)
            return min_pair

    def _bubble_down(self, idx: int) -> None:
        """
        Restore the heap-order property if necessary.
        """
        smallest = idx
        l = 2 * idx + 1
        r = 2 * idx + 2
        n = len(self._array)
        if l < n:
            if self._array[idx][0] > self._array[l][0]:
                smallest = l
        if r < n:
            if self._array[smallest][0] > self._array[r][0]:
                smallest = r
        if smallest != idx:
            self._array[idx], self._array[smallest] = self._array[smallest], self._array[idx]
            self._bubble_down(smallest)
