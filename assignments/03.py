'''
Singly Linked List
'''

class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class List:
  def __init__(self, start = None):
    self.start = start
  
  def __iter__(self):
    return ListIterator(self.start)
  
  def isEmpty(self):
    return self.start == None
  
  def insertAtStart(self, data):
    node = Node(data, self.start)
    self.start = node
  
  def insertAtLast(self, data):
    node = Node(data)

    if not self.isEmpty():
      currentNode = self.start

      while (currentNode.next is not None):
        currentNode = currentNode.next
      
      currentNode.next = node
    else:
      self.start = node
  
  def search(self, data):
    currentNode = self.start

    while (currentNode is not None):
      if currentNode.data == data:
        return currentNode
      
      currentNode = currentNode.next
    
    return None
  
  def insertAfter(self, data, newData):
    currentNode = self.start

    while (currentNode.next is not None):
      if currentNode.data == data:
        newNode = Node(newData, currentNode.next)
        currentNode.next = newNode

        return
      else:
        currentNode = currentNode.next
  
  def insertAfterNode(self, node: Node, newData):
    if (node is not None):
      newNode = Node(newData, node.next)
      node.next = newNode
  
  def print(self):
    currentNode = self.start

    if self.isEmpty(): return

    while (currentNode.next is not None):
      print(currentNode.data, end='->')
      currentNode = currentNode.next
    
    print(currentNode.data)
  
  def deleteFirst(self):
    if self.start is not None:
      self.start = self.start.next
  
  def deleteLast(self):
    if self.isEmpty(): return
    elif self.start.next is None: self.start = None
    else:
      currentNode = self.start

      while (currentNode.next.next is not None):
        currentNode = currentNode.next
      
      currentNode.next = None
  
  def delete(self, data):
    if self.isEmpty(): return
    elif self.start.next is None and self.start.data == data:
      self.start = None
    else:
      if self.start.data == data:
        self.start = self.start.next
      else:
        currentNode = self.start

        while (currentNode.next is not None):
          if currentNode.next.data == data:
            currentNode.next = currentNode.next.next

            return
            
          currentNode = currentNode.next

class ListIterator:
  def __init__(self, start):
    self.current = start

  def __iter__(self):
    return self
  
  def __next__(self):
    # stop iterating if current item is None
    if self.current is None:
      raise StopIteration
    
    # otherwise, increment current item and return the current item for iteration
    data = self.current.data
    self.current = self.current.next

    return data


myList = List()
myList.print()
myList.insertAtStart(20)
myList.insertAtStart(10)
myList.insertAtLast(30)
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
myList.insertAtLast(45)
print('iterating through for loop')
for item in myList:
  print(item, end=' ')

print('\n\nend of testing\n\n')
