import math

#1
print('\n#1\n')

class Person:
  def __init__(self, name: str = None, age: int = None):
    self.name = name
    self.age = age
  
  def show(self):
    print('name:', self.name, 'age:', self.age)


p = Person('Kaunaj', 29)

p.show()

#2
print('\n#2\n')

class Circle:
  def __init__(self, radius: float = None):
    self.radius = radius
  
  def getRadius(self):
    return self.radius
  
  def setRadius(self, radius: float = None):
    self.radius = radius
  
  def getArea(self):
    return math.pi * self.radius**2
  
  def getCircumference(self):
    return 2 * math.pi * self.radius


c = Circle(3.5)
print('initial radius:', c.getRadius())
print('initial area:', c.getArea())
print('initial circumference:', c.getCircumference())

c.setRadius(2.5)
print('modified radius:', c.getRadius())
print('modified area:', c.getArea())
print('modified circumference:', c.getCircumference())

#3
print('\n#3\n')

class Rectangle:
  def __init__(self, length: float = None, breadth: float = None):
    self.length = length
    self.breadth = breadth
  
  def setDimensions(self, length: float = None, breadth: float = None):
    self.length = length
    self.breadth = breadth
  
  def showDimensions(self):
    print('length:', self.length, end=', ')
    print('breadth:', self.breadth)
  
  def getArea(self):
    return self.length * self.breadth


r = Rectangle(2, 5)
print('initial dimensions:', end=' ')
r.showDimensions()
print('initial area:', r.getArea())

r.setDimensions(4.5, 3)
print('modified dimensions:', end=' ')
r.showDimensions()
print('modified area:', r.getArea())

#4
print('\n#4\n')

class Book:
  def __init__(self, bookId: str = None, title: str = None, price: float = None):
    self.bookId = bookId
    self.title = title
    self.price = price
  
  def showBookId(self):
    print(self.bookId)
  
  def showTitle(self):
    print(self.title)
  
  def showPrice(self):
    print(self.price)


b = Book('B110', 'Berserk Volume 1', 9.99)
b.showBookId()
b.showTitle()
b.showPrice()

#5
print('\n#5\n')

class Team:
  def __init__(self, members: list = None):
    self.members = members
  
  def setMembers(self, members: list = None):
    self.members = members
  
  def inputMembers(self):
    self.members = list(map(str, input('Input member names separated by commas:\n').split(',')))
  
  def displayMembers(self):
    print(self.members)


t = Team()
t.inputMembers()
t.displayMembers()
