'''
Binary Search Tree - I
'''

class Node:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

class BinarySearchTree:
  def __init__(self, root = None):
    self.root = root
  
  def insert(self, data):
    node = Node(data)

    if self.root is None:
      self.root = node
    else:
      currentNode = self.root

      while currentNode is not None:
        if currentNode.data == data:
          raise ValueError('Duplicate entries not allowed in BST')
        elif currentNode.data > data:
          # go left
          if currentNode.left is None:
            currentNode.left = node
            return
          
          currentNode = currentNode.left
        else:
          # go right
          if currentNode.right is None:
            currentNode.right = node
            return
          
          currentNode = currentNode.right
      

  def search(self, data):
    if self.root is None:
      return None
    
    currentNode = self.root

    while currentNode is not None:
      if currentNode.data == data:
        return currentNode
      elif currentNode.data > data:
        # go left
        currentNode = currentNode.left
      else:
        # go right
        currentNode = currentNode.right
    
    return None

  def traverse(self, type):
    traversedNodes = []

    if type == 'preOrder':
      self.traversePreOrder(self.root, traversedNodes)
    elif type == 'inOrder':
      self.traverseInOrder(self.root, traversedNodes)
    elif type == 'postOrder':
      self.traversePostOrder(self.root, traversedNodes)
    else:
      raise ValueError(f'Invalid traversal type: {type}')
    
    return traversedNodes

  def traversePreOrder(self, start, traversedNodes):
    if start.data not in traversedNodes:
      traversedNodes.append(start.data)
      # print(start.data)
    
    if start.left is not None:
      self.traversePreOrder(start.left, traversedNodes)

    if start.right is not None:
      self.traversePreOrder(start.right, traversedNodes)

  def traverseInOrder(self, start, traversedNodes):
    if start.left is not None:
      self.traverseInOrder(start.left, traversedNodes)

    if start.data not in traversedNodes:
      traversedNodes.append(start.data)
      # print(start.data)

    if start.right is not None:
      self.traverseInOrder(start.right, traversedNodes)

  def traversePostOrder(self, start, traversedNodes):    
    if start.left is not None:
      self.traversePostOrder(start.left, traversedNodes)

    if start.right is not None:
      self.traversePostOrder(start.right, traversedNodes)

    if start.data not in traversedNodes:
      traversedNodes.append(start.data)
      # print(start.data)


def test():
  root = Node(50)
  tree = BinarySearchTree(root)
  tree.insert(20)
  tree.insert(70)
  tree.insert(15)
  tree.insert(30)
  tree.insert(75)
  tree.insert(65)
  print('searching 15:', tree.search(15).data)
  print('searching 100:', tree.search(100))
  print('preOrder traversal:', tree.traverse('preOrder'))
  print('inOrder traversal:', tree.traverse('inOrder'))
  print('postOrder traversal:', tree.traverse('postOrder'))

test()
