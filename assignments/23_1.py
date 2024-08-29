'''
Graph - Adjacency Matrix (BFS and DFS)
'''

from importlib import import_module
G = import_module('23')
Q = import_module('12')
S = import_module('07')

class Graph(G.Graph):
  def search(self, source, type):
    print(f'search called with source: {source}, type: {type}')
    nodes = []

    if type == 'BFS':
      nodes = self.breadthFirstSearch(source)
    elif type == 'DFS':
      nodes = self.depthFirstSearch(source)
    else:
      raise ValueError(f'Invalid traversal type: {type}')
    
    return nodes
  
  def breadthFirstSearch(self, source):
    nodes = []
    visited = {}
    queue = Q.Queue()
    queue.enqueue(source)

    visited[source] = True
    

    while not queue.isEmpty():
      currentNode = queue.dequeue()

      nodes.append(currentNode)

      for index in range(len(self.list[currentNode])):
        neighbor, weight = self.list[currentNode][index]

        if neighbor not in visited and weight != 0:
          queue.enqueue(neighbor)

          visited[neighbor] = True

    return nodes

  def depthFirstSearch(self, source):
    nodes = []
    visited = {}
    stack = S.Stack()
    stack.push(source)

    visited[source] = True
    

    while not stack.isEmpty():
      currentNode = stack.pop()

      nodes.append(currentNode)

      for index in range(len(self.list[currentNode])):
        neighbor, weight = self.list[currentNode][index]

        if neighbor not in visited and weight != 0:
          stack.push(neighbor)

          visited[neighbor] = True

    return nodes


def test():
  graph = Graph(6)
  graph.print()
  graph.addEdge(0, 1)
  graph.addEdge(0, 2)
  graph.addEdge(1, 2)
  graph.addEdge(1, 3)
  graph.addEdge(2, 3)
  graph.addEdge(2, 4)
  graph.addEdge(3, 5)
  graph.addEdge(4, 5)
  graph.print()
  print(graph.search(0, 'BFS'))
  print(graph.search(0, 'DFS'))

test()
