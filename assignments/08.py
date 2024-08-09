'''
Stack By Inheriting List Class
'''

class Stack(list):
  def isEmpty(self):
    return len(self) == 0
  
  def push(self, data):
    self.append(data)
  
  def pop(self):
    if not self.isEmpty(): return super().pop()
    else: raise IndexError('Stack is empty')
  
  def peek(self):
    if not self.isEmpty(): return self[-1]
    else: raise IndexError('Stack is empty')
  
  def size(self):
    return len(self)
  
  def insert(self, pos, data):
    raise AttributeError('No attribute named \'insert\' in Stack')


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
# myStack.insert(0, 10) # will throw error
print('peek:', myStack.peek())
print('current size:', myStack.size())
