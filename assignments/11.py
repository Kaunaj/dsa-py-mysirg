'''
Stack By Inheriting Linked List Class
'''

import importlib
LinkedList = importlib.import_module('03')

class Stack(LinkedList.List):
  def __init__(self):
    super().__init__()
    self.length = 0
  
  def isEmpty(self):
    return super().isEmpty()

  def push(self, data):
    self.insertAtStart(data)
    self.length += 1

  def pop(self):
    if not self.isEmpty():
      data = self.start.data
      self.deleteFirst()
      self.length -= 1

      return data
    else:
      raise IndexError('Stack is empty')

  def peek(self):
    if not self.isEmpty(): return self.start.data
    else:
      raise IndexError('Stack is empty')

  def size(self):
    return self.length


def test():
  myStack = Stack()
  print('isEmpty:', myStack.isEmpty())
  print('current size:', myStack.size())
  myStack.push(1)
  print('isEmpty after pushing data:', myStack.isEmpty())
  print('peek:', myStack.peek())
  myStack.push(3)
  print('peek:', myStack.peek())
  print('current size:', myStack.size())
  print('popping:', myStack.pop())
  print('peek:', myStack.peek())
  myStack.push(2)
  print('peek:', myStack.peek())
  myStack.push(3)
  print('peek:', myStack.peek())
  print('current size:', myStack.size())

test()