'''
Deque Using List
'''

class Deque:
  def __init__(self):
    self.items = []
  
  def isEmpty(self):
    return len(self.items) == 0

  def insertFront(self, data):
    self.items.insert(0, data)

  def insertRear(self, data):
    self.items.append(data)

  def deleteFront(self):
    if not self.isEmpty():
      return self.items.pop(0)
    else:
      raise IndexError('Deque is empty')

  def deleteRear(self):
    if not self.isEmpty():
      return self.items.pop()
    else:
      raise IndexError('Deque is empty')

  def getFront(self):
    if not self.isEmpty():
      return self.items[0]
    else:
      raise IndexError('Deque is empty')

  def getRear(self):
    if not self.isEmpty():
      return self.items[-1]
    else:
      raise IndexError('Deque is empty')

  def size(self):
    return len(self.items)


def test():
  testDeque = Deque()
  print('isEmpty:', testDeque.isEmpty())
  print('current size:', testDeque.size())
  testDeque.insertFront(1)
  print('testDeque.insertFront(1)')
  print('isEmpty after inserting data in front:', testDeque.isEmpty())
  print('front:', testDeque.getFront(), end=', ')
  print('rear:', testDeque.getRear())
  testDeque.insertRear(3)
  print('testDeque.insertRear(3)')
  print('front:', testDeque.getFront(), end=', ')
  print('rear:', testDeque.getRear())
  print('current size:', testDeque.size())
  testDeque.insertRear(2)
  print('testDeque.insertRear(2)')
  print('front:', testDeque.getFront(), end=', ')
  print('rear:', testDeque.getRear())
  print('current size:', testDeque.size())
  print('deleting:', testDeque.deleteFront())
  print('front:', testDeque.getFront(), end=', ')
  print('rear:', testDeque.getRear())
  print('deleting:', testDeque.deleteRear())
  print('front:', testDeque.getFront(), end=', ')
  print('rear:', testDeque.getRear())
  testDeque.insertFront(2)
  print('testDeque.insertFront(2)')
  print('front:', testDeque.getFront(), end=', ')
  print('rear:', testDeque.getRear())
  testDeque.insertFront(1)
  print('testDeque.insertFront(1)')
  print('front:', testDeque.getFront(), end=', ')
  print('rear:', testDeque.getRear())
  print('current size:', testDeque.size())
  testDeque.insertRear(4)
  print('testDeque.insertRear(4)')
  print('front:', testDeque.getFront(), end=', ')
  print('rear:', testDeque.getRear())
  print('current size:', testDeque.size())

test()
