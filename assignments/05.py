'''
Circular Linked List
'''

class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class List:
  def __init__(self, last = None):
    self.last = last
  
  def __iter__(self):
    if self.last: return ListIterator(self.last)

  def isEmpty(self):
    return self.last == None

  def insertAtStart(self, data):
    node = Node(data)

    if self.isEmpty():
      node.next = node
      self.last = node
    else:
      node.next = self.last.next
      self.last.next = node

  def insertAtLast(self, data):
    node = Node(data)

    if self.isEmpty():
      node.next = node
      self.last = node
    else:
      node.next = self.last.next
      self.last.next = node
      self.last = node

  def insertAfterNode(self, node: Node, data):
    # print('insertAfterNode called, inserting', data, 'after', node.data)
    if node is not None:
      newNode = Node(data, node.next)
      node.next = newNode

      if node is self.last:
        self.last = newNode

  def search(self, data):
    # print('search called, searching', data)
    if self.isEmpty(): return None

    currentNode = self.last.next

    while currentNode is not self.last:
      if currentNode.data == data: return currentNode

      currentNode = currentNode.next
    
    return currentNode if currentNode.data == data else None

  def print(self):
    if self.isEmpty(): print('')
    else:
      currentNode = self.last.next

      while currentNode is not self.last:
        print(currentNode.data, end='->')
        currentNode = currentNode.next
      
      print(currentNode.data)

  def deleteFirst(self):
    if self.isEmpty(): return
    elif self.last.next is self.last: self.last = None
    else:
      self.last.next = self.last.next.next

  def deleteLast(self):
    if self.isEmpty(): return
    elif self.last.next is self.last: self.last = None
    else:
      currentNode = self.last.next

      while currentNode.next is not self.last:
        currentNode = currentNode.next
      
      currentNode.next = self.last.next
      self.last = currentNode

  def delete(self, data):
    # print('delete called, deleting', data)
    if self.isEmpty(): return None
    elif self.last.next is self.last:
      if self.last.data == data: self.last = None
    else:
      if self.last.next.data == data:
        self.last.next = self.last.next.next
      else:
        currentNode = self.last.next

        while currentNode is not self.last:
          # print('currentNode next data:', currentNode.next.data)
          if currentNode.next.data == data:
            # print('found data to delete, currentNode:', currentNode.data)

            if currentNode.next is self.last:
              # print('currentNode next is last')
              self.last = currentNode

            currentNode.next = currentNode.next.next

            # print('after deletion, last:', self.last.data)
            return
          
          currentNode = currentNode.next

class ListIterator:
  def __init__(self, last):
    self.current = last.next
    self.last = last
    self.lastReached = False

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.lastReached:
      raise StopIteration

    if self.current is self.last:
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
