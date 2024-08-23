'''
Binary Tree Traversal
'''

class Node:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
    self.visited = False

class BinaryTree:
  def __init__(self, root = None):
    self.root = root
  
  def traverse(self, start = None):
    if start is None:
      start = self.root
    
    if not start.visited:
      start.visited = True
      print(start.data)
    
    if start.left is None and start.right is None:
      return
    else:
      if start.left:
        self.traverse(start.left)
      
      if start.right:
        self.traverse(start.right)


def test():
  root = Node(50)
  n20 = Node(20)
  n30 = Node(30)
  n70 = Node(70)
  n60 = Node(60)
  n80 = Node(80)
  n100 = Node(100)
  n40 = Node(40)
  n90 = Node(90)
  n10 = Node(10)
  tree = BinaryTree(root)
  n90.left = n10
  n80.left = n40
  n80.right = n90
  n30.left = n80
  n30.right = n100
  n20.left = n70
  n20.right = n60
  root.left = n20
  root.right = n30
  tree.traverse()

test()
