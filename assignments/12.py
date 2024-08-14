'''
Queue Using List
'''

class Queue:
  def __init__(self):
    self.items = []
  
  def isEmpty(self):
    return len(self.items) == 0
  
  def enqueue(self, data):
    self.items.append(data)

  def dequeue(self):
    if not self.isEmpty():
      data = self.items[0]
      self.items.pop(0)

      return data
    
    raise IndexError('Queue is empty')

  def getFront(self):
    if not self.isEmpty(): return self.items[0]
    else:
      raise IndexError('Queue is empty')

  def getRear(self):
    if not self.isEmpty(): return self.items[-1]
    else:
      raise IndexError('Queue is empty')

  def size(self):
    return len(self.items)


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
