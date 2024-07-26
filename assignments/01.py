from array import array

class Solution:
  def sort(self, arr: array):
    return sorted(arr)
  
  def removeNonIntValues(self, arr: list):
    i = 0
    items = len(arr)

    while i < items:
      if type(arr[i]) != type(1):
        arr.pop(i)
        items = len(arr)
      else:
        i += 1
    
    return arr
  
  def average(self, arr: list = []):
    items = len(arr)

    if items == 0: return 0.0

    sumItems = sum(arr, 0)

    return sumItems / items
  
  @staticmethod
  def isPrime(num: int):
    i = 2

    while (i <= num // 2):
      if (num % i == 0): return False

      i += 1
    
    return True
  
  def firstNPrime(self, n: int = None):
    if n == 0 or n == None: return []

    primeNums = []
    count = 0
    i = 2

    while (count < n):
      if self.isPrime(i):
        primeNums.append(i)
        count += 1

      i += 1
    
    return primeNums
  
  def firstNFibonacci(self, n: int = None):
    if n == 0 or n == None: return []

    if n == 1: return [1]

    fibNums = [1, 1]
    count = 2
    i = 1

    while (count < n):
      fibNums.append(fibNums[i] + fibNums[i - 1])

      count += 1
      i += 1

    return fibNums


s = Solution()

#1
arr1 = array('i', [3, 2, 6, -7, 54, 42])
print(s.sort(arr1))

#2
arr2 = [1, 2, 'text', 7, 3.454, '222', 9, 2.1, 42, {'some': 'value'}]
print(s.removeNonIntValues(arr2))

#3
arr3 = [1, 2, 5, 3, 4, 8]
print(s.average(arr3))

#4
print(s.firstNPrime(10))

#5
print(s.firstNFibonacci(10))
