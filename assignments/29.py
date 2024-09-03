'''
Heap
'''

class EmptyHeapException(Exception):
  def __init__(self, message='Heap is empty'):
    self.message = message
  
  def __str__(self):
    return self.message

class Heap:
  def __init__(self):
    self.items = []
  
  def fromList(self, items):
    self.__init__()

    for item in items:
      self.insert(item)

  def insert(self, data):
    print('insert called with data:', data)
    self.items.append(data)

    size = len(self.items)
    index = size - 1

    while index > 0:
      parentIndex = (index - 1) // 2
      # print(f'index: {index}, parentIndex: {parentIndex}, items[index]: {self.items[index]}, items[parentIndex]: {self.items[parentIndex]}')

      if self.items[parentIndex] >= self.items[index]:
        break

      self.items[parentIndex], self.items[index] = self.items[index], self.items[parentIndex]
      index = parentIndex

  def delete(self):
    print('delete called')
    if len(self.items) == 0: raise EmptyHeapException()
    elif len(self.items) == 1: return self.items.pop()

    deletedData = self.items[0]
    self.items[0] = self.items.pop()
    index = 0

    while (2 * index) + 1 < len(self.items):
      maxChild, maxChildIndex = self.items[(2 * index) + 1], (2 * index) + 1

      if (2 * index) + 2 < len(self.items) and self.items[(2 * index) + 2] > maxChild:
        maxChild, maxChildIndex = self.items[(2 * index) + 2], (2 * index) + 2
      
      # print(f'index: {index}, items[index]: {self.items[index]}, maxChild: {maxChild} at index {maxChildIndex}')
      
      if self.items[index] >= maxChild:
        break
      
      # print('swapping', self.items[index], self.items[maxChildIndex])
      self.items[index], self.items[maxChildIndex] = self.items[maxChildIndex], self.items[index]
      index = maxChildIndex

    return deletedData

  def top(self):
    if len(self.items) == 0: raise EmptyHeapException()

    return self.items[0]

  def sort(self, array):
    self.fromList(array)
    print('self.items after calling fromList method:', self.items)
    sortedArray = []

    while len(self.items) > 0:
      sortedArray.insert(0, self.delete())
    
    return sortedArray

  def print(self):
    print('printing heap items')
    print(self.items)


def test():
  heap = Heap()
  # print(heap.top()) #! will throw error
  heap.insert(40)
  heap.insert(30)
  heap.insert(20)
  heap.insert(15)
  heap.insert(90)
  heap.insert(80)
  heap.insert(70)
  heap.insert(60)
  heap.insert(25)
  heap.print()
  print('current top is:', heap.top())
  heap.delete()
  heap.print()
  print('current top is:', heap.top())
  heap.delete()
  heap.print()
  print('current top is:', heap.top())
  array = [8, 7, 3, 9, 2, 5, 42, 30, 95, 16, 7]
  print(f'sorting {array}:', heap.sort(array))

test()
