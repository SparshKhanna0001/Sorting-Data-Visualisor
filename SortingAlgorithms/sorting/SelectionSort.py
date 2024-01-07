class SelectionSort():
  """
  SelectionSort implementation with callback for array structure changes.
  """

  def __init__(self):
      pass

  def sort(self, values, callback=None):
      if values is None:
          return
      self.selectionSort(values, callback)

  def selectionSort(self, array, callback=None):
      N = len(array)

      for i in range(0, N):
          # Find the index beyond i with a lower value than i
          swapIndex = i
          for j in range(i + 1, N):
              if array[j] < array[swapIndex]:
                  swapIndex = j

          self.swap(array, i, swapIndex)
          if callback:
              callback(array)  # Signal array structure changes

  def swap(self, ar, i, j):
      tmp = ar[i]
      ar[i] = ar[j]
      ar[j] = tmp


if __name__ == '__main__':
  """
  Example usage
  """
  def array_structure_changed_callback(arr):
      print(f"Array structure changed: {arr}")

  sorter = SelectionSort()
  array = [10, 4, 6, 8, 13, 2, 3]

  # Sorting with callback
  sorter.sort(array, array_structure_changed_callback)
  # Prints the sorted array
  print(array)
