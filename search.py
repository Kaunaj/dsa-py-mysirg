'''
Search algorithms (Linear and Binary)
'''

class Search:
  def linear(self, array, item):
    print(f'linear search called, searching for {item} in {array}')
    for index, element in enumerate(array):
      if element == item: return f'{item} found at index: {index}'
    
    return f'{item} not found'

  def binary(self, array, item):
    print(f'binary search called, searching for {item} in {array}')
    left = 0
    right = len(array) - 1
    
    while left <= right:
      middle = (left + right) // 2
      # print(f'left: {left}, right: {right}, middle: {middle}')

      if array[middle] == item: return f'{item} found at index: {middle}'
      elif array[middle] > item:
        right = middle - 1
      elif array[middle] < item:
        left = middle + 1
    
    return f'{item} not found'



def test():
  array = [8, 7, 3, 9, 2, 5, 42, 30, 95, 16, 7, 106, 84, 0, 25]
  print(Search().linear(array, 30))
  array.sort()
  print(Search().binary(array, 30))
  print(Search().binary(array, 0))
  print(Search().binary(array, 106))
  print(Search().binary(array, 23))

test()
