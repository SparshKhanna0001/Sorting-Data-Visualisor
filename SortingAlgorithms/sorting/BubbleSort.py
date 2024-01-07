class BubbleSort():
  def __init__(self, callback=None):
      self.callback = callback

  def notify_array_modified(self):
      if self.callback:
          self.callback()

  # ... (other methods remain unchanged)

  def sort(self, ar):
      # ... (existing code)

      sorted = False
      while True:
          sorted = True
          for i in range(1, len(ar)):
              if ar[i] < ar[i - 1]:
                  self.swap(ar, i - 1, i)
                  self.notify_array_modified()  # Notify when array is modified
                  sorted = False
          if sorted:
              break
  
  def swap(self, ar, i, j):
    tmp = ar[i]
    ar[i] = ar[j]
    ar[j] = tmp

if __name__ == '__main__':
  """
  Example usage
  """
  array = [10, 4, 6, 8, 13, 2, 3]
  sorter = BubbleSort()
  sorter.sort(array)
  # Prints:
  # [2, 3, 4, 6, 8, 10, 13]
  print(array)
