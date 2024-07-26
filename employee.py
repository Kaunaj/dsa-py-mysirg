class Employee:
  def __init__(self, empId=None, name=None, salary=None):
    self.empId = empId
    self.name = name
    self.salary = salary
  
  def getEmpId(self):
    return self.empId
  
  def getName(self):
    return self.name
  
  def getSalary(self):
    return self.salary
  
  def get(self, prop):
    return getattr(self, prop)
  
  def set(self, prop, value=None):
    setattr(self, prop, value)


emp = Employee(123, 'Kaunaj Banerjee', 180000)
print(emp.getEmpId(), emp.getName(), emp.getSalary())
print('before ->', emp.get('empId'), emp.get('name'), emp.get('salary'))

emp.set('empId', 456)
emp.set('name', 'Naruto Uzumaki')
emp.set('salary', 250000)
print('after ->', emp.get('empId'), emp.get('name'), emp.get('salary'))
