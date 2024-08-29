'''
Graph - Adjacency Matrix
'''

class Graph:
  def __init__(self, vertexCount = 0):
    self.vertexCount = vertexCount
    self.matrix = self.initializeMatrix(self.vertexCount)
  
  def initializeMatrix(self, vertexCount):
    matrix = []
    for i in range(vertexCount):
      matrix.append([])

      for j in range(vertexCount):
        matrix[i].append(0)
    
    return matrix
  
  def print(self):
    print('printing graph')
    for i in range(self.vertexCount):
      for j in range(self.vertexCount):
        print(self.matrix[i][j], end=' ')
      print()
  
  def addEdge(self, v1, v2, weight = 1):
    print(f'addEdge called with v1: {v1}, v2: {v2}, vertexCount: {self.vertexCount}')
    if v1 >= self.vertexCount or v2 >= self.vertexCount or v1 < 0 or v2 < 0:
      raise IndexError(f'Start and End vertex values must lie within 0 and {self.vertexCount - 1} (inclusive)')
    
    self.matrix[v1][v2] = weight
    self.matrix[v2][v1] = weight
  
  def removeEdge(self, v1, v2):
    print(f'removeEdge called with v1: {v1}, v2: {v2}, vertexCount: {self.vertexCount}')
    if v1 >= self.vertexCount or v2 >= self.vertexCount or v1 < 0 or v2 < 0:
      raise IndexError(f'Start and End vertex values must lie within 0 and {self.vertexCount - 1} (inclusive)')
    
    self.matrix[v1][v2] = 0
    self.matrix[v2][v1] = 0
  
  def hasEdge(self, v1, v2):
    print(f'hasEdge called with v1: {v1}, v2: {v2}, vertexCount: {self.vertexCount}')
    if v1 >= self.vertexCount or v2 >= self.vertexCount or v1 < 0 or v2 < 0:
      raise IndexError(f'Start and End vertex values must lie within 0 and {self.vertexCount - 1} (inclusive)')
    
    return self.matrix[v1][v2]


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
