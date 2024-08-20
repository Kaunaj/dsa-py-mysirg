'''
Priority Queue Using List
'''

class PriorityQueue:
  def __init__(self):
    self.items = []
  
  def isEmpty(self):
    return len(self.items) == 0
  
  def push(self, data, priority):
    for index in range(self.size()):
      _, currentPriority = self.items[index].values()

      if currentPriority > priority:
        self.items.insert(index, {'value': data, 'priority': priority})

        return
    
    self.items.append({'value': data, 'priority': priority})

  def pop(self):
    if not self.isEmpty(): return self.items.pop(0)['value']
    else:
      raise IndexError('Priority Queue is empty')

  def size(self):
    return len(self.items)


def test():
  priorityQueue = PriorityQueue()
  print('isEmpty:', priorityQueue.isEmpty())
  print('current size:', priorityQueue.size())
  priorityQueue.push(10, 1)
  print('isEmpty after inserting data:', priorityQueue.isEmpty())
  priorityQueue.push(30, 3)
  priorityQueue.push(20, 2)
  priorityQueue.push(50, 9)
  priorityQueue.push(25, 6)
  print('current size:', priorityQueue.size())
  print('order of processing:')
  while (not priorityQueue.isEmpty()):
    print(priorityQueue.pop(), end=' ')
  print()

test()
