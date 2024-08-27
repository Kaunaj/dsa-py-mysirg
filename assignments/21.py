'''
Binary Search Tree - II
'''

from importlib import import_module
BST = import_module('20')

class BinarySearchTree(BST.BinarySearchTree):
  def getMinSuccessor(self, start):
    if start is None: return

    parentSuccessor = start
    successor = parentSuccessor.right

    while successor is not None and successor.left is not None:
      # print(f'successor: {successor.data}')
      parentSuccessor = successor
      successor = successor.left

    # print(f'final successor: {successor.data}')
    return parentSuccessor, successor

  def getMaxPredecessor(self, start):
    if start is None: return

    parentPredecessor = start
    predecessor = parentPredecessor.left

    while predecessor is not None and predecessor.right is not None:
      # print(f'predecessor: {predecessor.data}')
      parentPredecessor = predecessor
      predecessor = predecessor.right

    return parentPredecessor, predecessor
  
  def delete(self, data):
    if self.root.data == data:
      currentNode = self.root

      if currentNode.left is not None and currentNode.right is not None:
        # 2 children
        # print('2 children')
        parentPredecessor, predecessor = self.getMaxPredecessor(currentNode)
        currentNode.data = predecessor.data

        if predecessor.left is not None:
          # predecessor has 1 child
          currentNode.left = predecessor.left
        else:
          # predecessor has no child
          predecessor = None
      elif currentNode.left is not None or currentNode.right is not None:
        # 1 child
        # print('1 child')
        child = None

        if currentNode.left is not None:
          child = currentNode.left
        elif currentNode.right is not None:
          child = currentNode.right
        
        self.root = child
      else:
        # no child
        # print('no child')
        self.root = None

      return
    
    parentNode = self.root
    currentNode = None

    if parentNode.data > data:
      currentNode = parentNode.left
    elif parentNode.data < data:
      currentNode = parentNode.right

    while currentNode is not None:
      # print(f'parentNode: {parentNode.data}, currentNode: {currentNode.data}')
      if currentNode.data == data:
        # print(f'found data to delete: {currentNode.data}')
        if currentNode.left is not None and currentNode.right is not None:
          # 2 children
          # print('2 children')
          parentPredecessor, predecessor = self.getMaxPredecessor(currentNode)
          currentNode.data = predecessor.data

          if predecessor.left is not None:
            # predecessor has 1 child
            parentPredecessor.right = predecessor.left
          else:
            # predecessor has no child
            predecessor = None
        elif currentNode.left is not None or currentNode.right is not None:
          # 1 child
          # print('1 child')
          child = None

          if currentNode.left is not None:
            child = currentNode.left
          elif currentNode.right is not None:
            child = currentNode.right
          
          if currentNode is parentNode.left:
            parentNode.left = child
          elif currentNode is parentNode.right:
            parentNode.right = child
        else:
          # no child
          # print('no child')
          if currentNode is parentNode.left:
            parentNode.left = None
          elif currentNode is parentNode.right:
            parentNode.right = None

        return

      # print('still searching...')
      parentNode = currentNode
      # print(f'parentNode: {parentNode.data}')

      if parentNode.data > data:
        # go left
        currentNode = parentNode.left
      elif parentNode.data < data:
        # go right
        currentNode = parentNode.right
      
      # print(f'currentNode: {currentNode.data}')


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
  print('deleting 30')
  tree.delete(30)
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('deleting 15')
  tree.delete(15)
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('deleting 70')
  tree.delete(70)
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('deleting root 50')
  tree.delete(50)
  print('inOrder traversal:', tree.traverse('inOrder'))

test()
