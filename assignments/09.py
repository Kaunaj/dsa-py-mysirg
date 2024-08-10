'''
Stack Using Linked List Concept
'''

class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self, start = None):
    self.start = start
    self.length = 0

  def isEmpty(self):
    return self.start == None

  def push(self, data):
    node = Node(data, self.start)
    self.start = node
    self.length += 1

  def pop(self):
    if not self.isEmpty():
      data = self.start.data
      self.start = self.start.next
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


myStack = Stack()
print('current size:', myStack.size())
myStack.push(1)
print('peek:', myStack.peek())
myStack.push(3)
print('peek:', myStack.peek())
print('current size:', myStack.size())
myStack.pop()
print('peek:', myStack.peek())
myStack.push(2)
print('peek:', myStack.peek())
myStack.push(3)
print('peek:', myStack.peek())
print('current size:', myStack.size())
