'''
Selection Sort
'''

class SelectionSort:
  def __init__(self, array):
    self.array = array
  
  def normal(self):
    print('selectionSort called with array:', self.array)
    start = 0
    end = len(self.array)

    while start < end - 1:
      index = start + 1
      minIndex = start

      while index < end:
        if self.array[index] < self.array[minIndex]:
          minIndex = index

        index += 1
      
      if minIndex != start:
        self.array[start], self.array[minIndex] = self.array[minIndex], self.array[start]
      
      start += 1

  def print(self):
    print(self.array)


def test():
  array1 = SelectionSort([8, 7, 3, 9, 2, 5, 42, 30, 95, 16])
  array1.normal()
  array1.print()

test()
