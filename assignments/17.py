'''
Priority Queue Using Linked List Concept
'''

class Node:
  def __init__(self, data = None, priority = None, next = None):
    self.data = data
    self.priority = priority
    self.next = next

class PriorityQueue:
  def __init__(self):
    self.start = None
    self.length = 0
  
  def isEmpty(self):
    return self.length == 0

  def push(self, data, priority):
    node = Node(data, priority)

    if self.isEmpty():
      self.start = node
    elif self.length == 1:
      if self.start.priority > priority:
        self.start.next = node
      else:
        node.next = self.start
        self.start = node
    else:
      if self.start.priority > priority:
        node.next = self.start
        self.start = node
      else:
        currentNode = self.start

        while currentNode.next is not None and currentNode.next.priority <= priority:
          currentNode = currentNode.next
        
        node.next = currentNode.next
        currentNode.next = node
    
    self.length += 1

  def pop(self):
    if self.isEmpty():
      raise IndexError('Priority Queue is empty')
    
    data = self.start.data

    if self.length == 1:
      self.start = None
    else:
      self.start = self.start.next
    
    self.length -= 1

    return data

  def size(self):
    return self.length


def test():
  priorityQueue = PriorityQueue()
  print('isEmpty:', priorityQueue.isEmpty())
  print('current size:', priorityQueue.size())
  priorityQueue.push(10, 1)
  print('isEmpty after inserting data:', priorityQueue.isEmpty())
  priorityQueue.push(30, 3)
  priorityQueue.push(20, 2)
  priorityQueue.push(50, 9)
  priorityQueue.push(25, 6)
  priorityQueue.push(5, 0)
  print('current size:', priorityQueue.size())
  print('order of processing:')
  while (not priorityQueue.isEmpty()):
    print(priorityQueue.pop(), end=' ')
  print()

test()
