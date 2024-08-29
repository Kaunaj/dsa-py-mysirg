'''
Graph - Adjacency List
'''

class Graph:
  def __init__(self, vertexCount = 0):
    self.vertexCount = vertexCount
    self.list = self.initializeList(self.vertexCount)
  
  def initializeList(self, vertexCount):
    edges = {}

    for i in range(vertexCount):
      edges[i] = []
    
    return edges
  
  def print(self):
    for edge in self.list:
      print(edge, '->', ' '.join(map(str, self.list[edge])))
  
  def addEdge(self, v1, v2, weight = 1):
    print(f'addEdge called with v1: {v1}, v2: {v2}, vertexCount: {self.vertexCount}')
    if v1 >= self.vertexCount or v2 >= self.vertexCount or v1 < 0 or v2 < 0:
      raise IndexError(f'Start and End vertex values must lie within 0 and {self.vertexCount - 1} (inclusive)')
    
    self.list[v1].append((v2, weight))
    self.list[v2].append((v1, weight))
  
  def removeEdge(self, v1, v2):
    print(f'removeEdge called with v1: {v1}, v2: {v2}, vertexCount: {self.vertexCount}')
    if v1 >= self.vertexCount or v2 >= self.vertexCount or v1 < 0 or v2 < 0:
      raise IndexError(f'Start and End vertex values must lie within 0 and {self.vertexCount - 1} (inclusive)')
    
    for neighbor in self.list[v1]:
      (edge, weight) = neighbor
      
      if edge == v2:
        self.list[v1].remove(neighbor)
        self.list[v2].remove((v1, weight))
  
  def hasEdge(self, v1, v2):
    print(f'hasEdge called with v1: {v1}, v2: {v2}, vertexCount: {self.vertexCount}')
    if v1 >= self.vertexCount or v2 >= self.vertexCount or v1 < 0 or v2 < 0:
      raise IndexError(f'Start and End vertex values must lie within 0 and {self.vertexCount - 1} (inclusive)')
    
    return v2 in map(lambda x: x[0], self.list[v1])


def test():
  graph = Graph(4)
  graph.print()
  graph.addEdge(0, 2)
  graph.addEdge(1, 2, -50)
  graph.addEdge(1, 3, 10)
  graph.addEdge(3, 0, 42)
  graph.print()
  print(graph.hasEdge(2, 1))
  # graph.addEdge(4, 2, 5) #! will throw error
  graph.removeEdge(1, 2)
  graph.print()
  print(graph.hasEdge(2, 1))

# test()
