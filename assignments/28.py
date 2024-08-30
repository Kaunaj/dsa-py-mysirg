'''
Merge Sort
'''

class MergeSort:
  def __init__(self, array):
    self.array = array
  
  def process(self):
    print('mergeSort called with array:', self.array)
    self.array = self.sort(self.array)
  
  def sort(self, subArray):
    print('sort called with subArray:', subArray)
    if len(subArray) <= 1: return subArray
    else:
      left = 0
      right = len(subArray)
      middle = (left + right) // 2

      # print(f'left: {left}, right: {right}, middle: {middle}, subArray[left:middle]: {subArray[left:middle]}, subArray[middle:right]: {subArray[middle:right]}')
      return self.merge(self.sort(subArray[left:middle]), self.sort(subArray[middle:right]))
  
  def merge(self, array1, array2):
    print('merge called with', array1, array2)
    p1 = 0
    p2 = 0
    mergedArray = []

    while p1 + p2 < len(array1) + len(array2):
      # print(f'p1: {p1}, p2: {p2}, current mergedArray: {mergedArray}, og array: {array1, array2}')
      if p1 < len(array1) and p2 < len(array2) and array1[p1] < array2[p2]:
        # print('p1 < p2')
        mergedArray.append(array1[p1])

        p1 += 1
      elif p1 < len(array1) and p2 < len(array2) and array1[p1] > array2[p2]:
        # print('p1 > p2')
        mergedArray.append(array2[p2])

        p2 += 1
      else:
        # print('else')
        if p1 < len(array1):
          mergedArray.append(array1[p1])
          p1 += 1
        
        if p2 < len(array2):
          mergedArray.append(array2[p2])
          p2 += 1
    
    # print('returning mergedArray:', mergedArray)
    return mergedArray
  
  def print(self):
    print(self.array)


def test():
  array1 = MergeSort([8, 7, 3, 9, 2, 5, 42, 30, 95, 16, 7])
  array1.process()
  array1.print()

test()
