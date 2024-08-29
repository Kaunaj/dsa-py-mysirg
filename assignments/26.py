'''
Insertion Sort
'''

class InsertionSort:
  def __init__(self, array):
    self.array = array
  
  def normal(self):
    print('insertionSort called with array:', self.array)
    start = 1
    end = len(self.array)

    while start < end:
      temp = self.array[start]
      index = start - 1

      while index >= 0:
        # print(f'start: {start}, temp: {temp}, index: {index}')
        if self.array[index] <= temp:
          break
        else:
          self.array[index + 1] = self.array[index]
          self.array[index] = None
          index -= 1
      
      if self.array[index + 1] is None:
        self.array[index + 1] = temp
      
      start += 1

  def print(self):
    print(self.array)


def test():
  array1 = InsertionSort([8, 7, 3, 9, 2, 5, 42, 30, 95, 16, 7])
  array1.normal()
  array1.print()

test()
