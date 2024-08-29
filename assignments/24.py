'''
Bubble Sort (Normal and Modified)
'''

class BubbleSort:
  def __init__(self, array):
    self.array = array
  
  def normal(self):
    print('bubbleSortNormal called with array:', self.array)
    start = 0
    end = len(self.array) - 1

    while start < end - 1:
      index = 0

      while index < end:
        if self.array[index] > self.array[index + 1]:
          # print('swapping:', array[index], array[index + 1])
          self.array[index], self.array[index + 1] = self.array[index + 1], self.array[index]
        else:
          index += 1
      
      start += 1

  def modified(self):
    print('bubbleSortModified called with array:', self.array)
    start = 0
    end = len(self.array) - 1

    while start < end - 1:
      index = 0
      swaps = 0

      while index < end:
        if self.array[index] > self.array[index + 1]:
          # print('swapping:', array[index], array[index + 1])
          self.array[index], self.array[index + 1] = self.array[index + 1], self.array[index]
          swaps += 1
        else:
          index += 1
      
      if swaps == 0:
        print('no swaps happened, ending')
        break
      
      start += 1
  
  def print(self):
    print(self.array)


def test():
  array1 = BubbleSort([8, 7, 3, 9, 2, 5, 42, 30, 95, 16])
  array1.normal()
  array1.print()
  array2 = BubbleSort([8, 7, 3, 9, 2, 5, 42, 30, 95, 16])
  array2.modified()
  array2.print()

test()
