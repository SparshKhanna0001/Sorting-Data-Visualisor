'''
 * @file   InsertionSort.py
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Armin Zare Zadeh, ali.a.zarezadeh@gmail.com
 * @date   27 Jun 2020
 * @version 0.1
 * @brief   Insertion sort implementation
'''

import sys
class InsertionSort():
  def __init__(self, callback=None):
      self.callback = callback

  def notify_array_modified(self):
      if self.callback:
          self.callback()

  def sort(self, values):
      self.insertionSort(values)

  def insertionSort(self, ar):
      if ar is None:
          return

      for i in range(1, len(ar)):
          j = i
          while j > 0 and ar[j] < ar[j - 1]:
              self.swap(ar, j - 1, j)
              j -= 1
              self.notify_array_modified()  # Notify when array is modified

  def swap(self, ar, i, j):
      tmp = ar[i]
      ar[i] = ar[j]
      ar[j] = tmp


if __name__ == '__main__':
  """
  Example usage
  """
  sorter = InsertionSort()
  array = [10, 4, 6, 8, 13, 2, 3]
  sorter.sort(array)
  # Prints:
  # [2, 3, 4, 6, 8, 10, 13]
  print(array)
