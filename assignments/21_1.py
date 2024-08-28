'''
Binary Search Tree - II (Recursion)
'''

from importlib import import_module
BST = import_module('20')

class BinarySearchTree(BST.BinarySearchTree):
  def getMaxValue(self, start):
    if start is None: return None

    currentNode = start

    while currentNode.right is not None:
      currentNode = currentNode.right
    
    return currentNode.data

  def getMinValue(self, start):
    if start is None: return None

    currentNode = start

    while currentNode.left is not None:
      currentNode = currentNode.left
    
    return currentNode.data

  def delete(self, data):
    self.root = self.rdelete(self.root, data)

  def rdelete(self, start, data):
    # print(f'rdelete called with start: {start.data if start else None}, data to delete: {data}')
    if start is None: return start

    if start.data > data:
      # print('go left')
      start.left = self.rdelete(start.left, data)
    elif start.data < data:
      # print('go right')
      start.right = self.rdelete(start.right, data)
    else:
      # print('found data to delete:', data)
      if start.left is None:
        # print('returning right child')
        return start.right
      elif start.right is None:
        # print('returning left child')
        return start.left
      else:
        # print('2 children')
        start.data = self.getMaxValue(start.left)
        start.left = self.rdelete(start.left, start.data)
      
    # print('returning start:', start.data)
    return start
  
  def size(self):
    return len(self.traverse('inOrder'))


def test():
  root = BST.Node(50)
  tree = BinarySearchTree(root)
  tree.insert(20)
  tree.insert(70)
  tree.insert(15)
  tree.insert(10)
  tree.insert(30)
  tree.insert(75)
  tree.insert(65)
  tree.insert(60)
  tree.insert(67)
  tree.insert(72)
  tree.insert(80)
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('current size:', tree.size())
  print('deleting 30')
  tree.delete(30)
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('current size:', tree.size())
  print('deleting 15')
  tree.delete(15)
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('current size:', tree.size())
  print('deleting 70')
  tree.delete(70)
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('current size:', tree.size())
  print('deleting root 50')
  tree.delete(50)
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('current size:', tree.size())

test()
