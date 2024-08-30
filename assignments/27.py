'''
Quick Sort
'''

class QuickSort:
  def __init__(self, array):
    self.array = array
  
  def process(self):
    print('quickSort called with array:', self.array)

    self.array = self.rprocess(self.array)
  
  def rprocess(self, array):
    print('rprocess called with array', array)
    if len(array) <= 1: return array

    array, curr = self.quick(array).values()
    
    # print(f'recursive call::::: array[0:curr]: {array[0:curr]}, array[curr]: {array[curr]}, array[curr + 1:len(array)]: {array[curr + 1:len(array)]}')
    return self.rprocess(array[0:curr]) + [array[curr]] + self.rprocess(array[curr + 1:len(array)])
  
  def quick(self, subArray):
    print('quick called with subArray', subArray)
    left = 0
    right = len(subArray) - 1
    curr = 0

    while left < right:
      # print(f'left: {left}, right: {right}, curr: {curr}', subArray[right], subArray[curr])
      while right > 0 and subArray[right] >= subArray[curr]:
        right -= 1
      # print(f'after right while: right={right}, curr={curr}')
      
      if curr != right + 1:
        subArray[right], subArray[curr] = subArray[curr], subArray[right]
        curr = right

      while left < right and subArray[left] <= subArray[curr]:
        left += 1
      # print(f'after left while: left={left}, curr={curr}')
      
      if curr != left - 1:
        subArray[left], subArray[curr] = subArray[curr], subArray[left]
        curr = left
    
    # print('returning from quick:', {'subArray': subArray, 'curr': curr})
    return {'subArray': subArray, 'curr': curr}

  def print(self):
    print(self.array)


def test():
  array1 = QuickSort([8, 7, 3, 9, 2, 5, 42, 30, 95, 16, 7])
  array1.process()
  array1.print()

test()
