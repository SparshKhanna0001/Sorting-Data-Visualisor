'''
 * @file   QuickSort.py
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Armin Zare Zadeh, ali.a.zarezadeh@gmail.com
 * @date   28 Jun 2020
 * @version 0.1
 * @brief   Quick sort implementation
'''

import sys

class QuickSort():
    """
    QuickSort implementation with callback for array structure changes.
    """

    def __init__(self):
        pass

    def sort(self, values, callback=None):
        if values is None:
            return
        self.quicksort(values, 0, len(values) - 1, callback)

    def quicksort(self, ar, lo, hi, callback=None):
        if lo < hi:
            splitPoint = self.partition(ar, lo, hi)
            self.quicksort(ar, lo, splitPoint - 1, callback)
            self.quicksort(ar, splitPoint + 1, hi, callback)
            if callback:
                callback(ar)  # Trigger callback after partitioning

    def partition(self, ar, lo, hi):
        pivot = ar[hi]
        i = lo - 1
        for j in range(lo, hi):
            if ar[j] < pivot:
                i += 1
                self.swap(ar, i, j)
        self.swap(ar, i + 1, hi)
        return i + 1

    def swap(self, ar, i, j):
        tmp = ar[i]
        ar[i] = ar[j]
        ar[j] = tmp


    def array_structure_changed_callback(arr):
        print(f"Array structure changed: {arr}")


if __name__ == '__main__':
  """
  Example usage
  """
  sorter = QuickSort()
  array = [10, 4, 6, 4, 8, -13, 2, 3]

  # Sorting with callback
  sorter.sort(array, array_structure_changed_callback)
  # Prints the sorted array
  print(array)
