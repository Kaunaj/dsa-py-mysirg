'''
Doubly Linked List
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
    node = Node(data, None, self.start)

    if not self.isEmpty():
      self.start.prev = node
    
    self.start = node

  def insertAtLast(self, data):
    node = Node(data)

    if self.isEmpty():
      self.start = node
    else:
      currentNode = self.start

      while currentNode.next:
        currentNode = currentNode.next
      
      currentNode.next = node
      node.prev = currentNode

  def insertAfterNode(self, node: Node, data):
    if node is not None:
      newNode = Node(data, node, node.next)
      node.next = newNode
      
      if newNode.next:
        newNode.next.prev = newNode

  def search(self, data):
    if self.isEmpty(): return None

    currentNode = self.start

    while currentNode:
      if currentNode.data == data:
        return currentNode
      
      currentNode = currentNode.next
    
    return None

  def print(self):
    if self.isEmpty(): return

    currentNode = self.start

    while currentNode.next:
      print(currentNode.data, end='->')
      currentNode = currentNode.next
    
    print(currentNode.data)

  def deleteFirst(self):
    if self.isEmpty(): return

    if self.start.next is None:
      self.start = None
    else:
      self.start = self.start.next
      self.start.prev = None

  def deleteLast(self):
    if self.isEmpty(): return

    if self.start.next is None:
      self.start = None
    else:
      currentNode = self.start

      while currentNode.next:
        currentNode = currentNode.next
      
      currentNode.prev.next = None

  def delete(self, data):
    if self.isEmpty(): return

    if self.start.next is None:
      if self.start.data == data:
        self.start = None
    else:
      if self.start.data == data:
        self.start.next.prev = None
        self.start = self.start.next
      else:
        currentNode = self.start

        while currentNode:
          if currentNode.data == data:
            currentNode.prev.next = currentNode.next

            if currentNode.next:
              currentNode.next.prev = currentNode.prev
            
            return
          
          currentNode = currentNode.next

class ListIterator:
  def __init__(self, start):
    self.current = start
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.current is None:
      raise StopIteration
    
    data = self.current.data
    self.current = self.current.next

    return data


myList = List()
myList.print()
myList.insertAtStart(20)
myList.insertAtStart(10)
myList.insertAtLast(30)
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
myList.insertAfterNode(myList.search(35), 45)
myList.insertAtStart(5)
myList.print()
print('iterating through for loop')
for item in myList:
  print(item, end=' ')

print('\n\nend of testing\n\n')
