"""
Implementation of basic binary heaps.
"""


class MaxHeap:
  """
  Implementation of a max binary heap.
  """

  def __init__(self):
    """
    Instantiate the max heap.
    """
    self._array: list[tuple] = []

  def insert(self, key, value) -> None:
    """
    """
    self._array.append((key, value))
    if len(self._array) > 1:
      self._bubble_up()

  def _bubble_up(self):
    """
    """
    n = len(self._array) - 1
    while self._array[n // 2][0] < self._array[n][0]:
        self._array[ n // 2], self._array[n] = self._array[n], self._array[n//2]
        n = n//2

  def remove(self) -> tuple:
    """
    """
    max_pair = self._array[0]
    self._array[0] = self._array[-1]
    self._array.pop()
    self._bubble_down(0)
    return max_pair

  def _bubble_down(self, i):
    """
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(self._array):
        if self._array[i][0] < self._array[l][0]:
            largest = l
    if r < len(self._array):
        if self._array[largest][0] < self._array[r][0]:
            largest = r
    if largest != i:
        self._array[i], self._array[largest] = self._array[largest], self._array[i]
        self._bubble_down(largest)


class MinHeap:
  """
  Implementation of a min binary heap.
  """

  def __init__(self):
    """
    Instantiate the min heap.
    """
    self._array: list[tuple] = []

  def insert(self, key, value) -> None:
    """
    """
    self._array.append((key, value))
    if len(self._array) > 1:
      self._bubble_up()

  def _bubble_up(self):
    """
    """
    n = len(self._array) - 1
    while self._array[n // 2][0] > self._array[n][0]:
        self._array[ n // 2], self._array[n] = self._array[n], self._array[n//2]
        n = n//2

  def remove(self) -> tuple:
    """
    """
    max_pair = self._array[0]
    self._array[0] = self._array[-1]
    self._array.pop()
    self._bubble_down(0)
    return max_pair

  def _bubble_down(self, i):
    """
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < len(self._array):
        if self._array[i][0] > self._array[l][0]:
            largest = l
    if r < len(self._array):
        if self._array[largest][0] > self._array[r][0]:
            largest = r
    if largest != i:
        self._array[i], self._array[largest] = self._array[largest], self._array[i]
        self._bubble_down(largest)