'''
Stack Using List
'''

class Stack:
  def __init__(self):
    self.items = []
  
  def isEmpty(self):
    return len(self.items) == 0

  def push(self, data):
    self.items.append(data)

  def pop(self):
    if not self.isEmpty(): return self.items.pop()
    else: raise IndexError('Stack is empty')

  def peek(self):
    if not self.isEmpty(): return self.items[-1]
    else: raise IndexError('Stack is empty')

  def size(self):
    return len(self.items)


myStack = Stack()
print('current size:', myStack.size())
myStack.push(1)
print('peek:', myStack.peek())
myStack.push(3)
print('peek:', myStack.peek())
myStack.pop()
myStack.push(2)
print('peek:', myStack.peek())
myStack.push(3)
print('peek:', myStack.peek())
print('current size:', myStack.size())
