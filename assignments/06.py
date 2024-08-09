'''
Circular Doubly Linked List
'''

class Node:
  def __init__(self, data = None, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next
  
class List:
  def __init__(self, start = None):
    self.start = start
  
  def __iter__(self):
    return ListIterator(self.start)

  def isEmpty(self):
    return self.start == None

  def insertAtStart(self, data):
    node = Node(data)

    if self.isEmpty():
      node.prev = node
      node.next = node
    else:
      node.prev = self.start.prev
      node.next = self.start
      self.start.prev.next = node
      self.start.prev = node
    
    self.start = node

  def insertAtLast(self, data):
    node = Node(data)

    if self.isEmpty():
      node.prev = node
      node.next = node
      self.start = node
    else:
      node.prev = self.start.prev
      node.next = self.start
      self.start.prev.next = node
      self.start.prev = node

  def insertAfterNode(self, node: Node, data):
    if node is not None:
      newNode = Node(data, node, node.next)
      node.next.prev = newNode
      node.next = newNode
  
  def search(self, data):
    if self.isEmpty(): return None

    currentNode = self.start

    while currentNode.next is not self.start:
      if currentNode.data == data: return currentNode

      currentNode = currentNode.next
    
    return currentNode if currentNode.data == data else None

  def print(self):
    if self.isEmpty(): print('')
    else:
      currentNode = self.start

      while currentNode.next is not self.start:
        print(currentNode.data, end='->')
        
        currentNode = currentNode.next
      
      print(currentNode.data)

  def deleteFirst(self):
    if self.isEmpty(): return
    elif self.start.next is self.start: self.start = None
    else:
      self.start.prev.next = self.start.next
      self.start.next.prev = self.start.prev
      self.start = self.start.next

  def deleteLast(self):
    if self.isEmpty(): return
    elif self.start.next is self.start: self.start = None
    else:
      self.start.prev.prev.next = self.start
      self.start.prev = self.start.prev.prev

  def delete(self, data):
    if self.isEmpty(): return
    elif self.start.next is self.start:
      if self.start.data == data:
        self.start = None
    else:
      if self.start.data == data:
        self.start.prev.next = self.start.next
        self.start.next.prev = self.start.prev
        self.start = self.start.next
        
        return
      
      currentNode = self.start

      while currentNode.next is not self.start:
        if currentNode.next.data == data:
          currentNode.next.next.prev = currentNode
          currentNode.next = currentNode.next.next

          return
        
        currentNode = currentNode.next

class ListIterator:
  def __init__(self, start):
    self.current = start
    self.start = start
    self.lastReached = False
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.current is None or self.lastReached:
      raise StopIteration
    
    if self.current.next is self.start:
      self.lastReached = True
    
    data = self.current.data
    self.current = self.current.next

    return data


myList = List()
myList.print()
myList.insertAtStart(20)
myList.print()
myList.insertAtStart(10)
myList.print()
myList.insertAtLast(30)
myList.print()
myList.insertAfterNode(myList.search(10), 15)
myList.insertAfterNode(myList.search(20), 25)
myList.print()
myList.delete(20)
print('testing myList.delete(20)')
myList.print()
myList.deleteFirst()
print('testing myList.deleteFirst()')
myList.print()
myList.deleteLast()
print('testing myList.deleteLast()')
myList.print()

myList.insertAtLast(35)
print('inserted 35 at last')
myList.print()
myList.insertAfterNode(myList.search(35), 45)
myList.insertAtStart(5)
print('inserted 5 at start')
myList.print()
print('iterating through for loop')
for item in myList:
  print(item, end=' ')

print('\n\nend of testing\n\n')
