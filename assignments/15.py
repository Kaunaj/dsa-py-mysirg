'''
Deque Using Doubly Linked List Concept
'''

class Node:
  def __init__(self, data = None, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next

class Deque:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0
  
  def isEmpty(self):
    return self.length == 0
  
  def insertFront(self, data):
    node = Node(data)

    if self.isEmpty():
      self.rear = node
    else:
      node.next = self.front
      self.front.prev = node
    
    self.front = node
    self.length += 1

  def insertRear(self, data):
    node = Node(data)

    if self.isEmpty():
      self.front = node
    else:
      node.prev = self.rear
      self.rear.next = node
      
    self.rear = node
    self.length += 1

  def deleteFront(self):
    if not self.isEmpty():
      data = self.front.data

      if self.length == 1:
        self.front = None
        self.rear = None
      else:
        self.front.next.prev = None
        self.front = self.front.next

      self.length -= 1
      
      return data
    else:
      raise IndexError('Deque is empty')

  def deleteRear(self):
    if not self.isEmpty():
      data = self.rear.data

      if self.length == 1:
        self.front = None
        self.rear = None
      else:
        self.rear.prev.next = None
        self.rear = self.rear.prev

      self.length -= 1

      return data
    else:
      raise IndexError('Deque is empty')

  def getFront(self):
    if not self.isEmpty():
      return self.front.data
    else:
      raise IndexError('Deque is empty')

  def getRear(self):
    if not self.isEmpty():
      return self.rear.data
    else:
      raise IndexError('Deque is empty')

  def size(self):
    return self.length


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
