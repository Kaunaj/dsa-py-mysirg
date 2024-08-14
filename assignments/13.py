'''
Queue Using Linked List Concept
'''

class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0
  
  def isEmpty(self):
    return self.length == 0
  
  def enqueue(self, data):
    node = Node(data)

    if self.isEmpty():
      self.front = node
    else:
      self.rear.next = node
    
    self.rear = node
    self.length += 1

  def dequeue(self):
    if not self.isEmpty():
      data = self.front.data

      if self.length == 1:
        self.front = None
        self.rear = None
      else:
        self.front = self.front.next
      
      self.length -= 1
      
      return data
    else:
      raise IndexError('Queue is empty')

  def getFront(self):
    if not self.isEmpty(): return self.front.data
    else:
      raise IndexError('Queue is empty')

  def getRear(self):
    if not self.isEmpty(): return self.rear.data
    else:
      raise IndexError('Queue is empty')

  def size(self):
    return self.length


def test():
  myQueue = Queue()
  print('isEmpty:', myQueue.isEmpty())
  print('current size:', myQueue.size())
  myQueue.enqueue(1)
  print('isEmpty after enqueueing data:', myQueue.isEmpty())
  print('front:', myQueue.getFront(), end=', ')
  print('rear:', myQueue.getRear())
  myQueue.enqueue(3)
  print('front:', myQueue.getFront(), end=', ')
  print('rear:', myQueue.getRear())
  print('current size:', myQueue.size())
  print('dequeueing:', myQueue.dequeue())
  print('front:', myQueue.getFront(), end=', ')
  print('rear:', myQueue.getRear())
  myQueue.enqueue(2)
  print('front:', myQueue.getFront(), end=', ')
  print('rear:', myQueue.getRear())
  myQueue.enqueue(1)
  print('front:', myQueue.getFront(), end=', ')
  print('rear:', myQueue.getRear())
  print('current size:', myQueue.size())

test()
