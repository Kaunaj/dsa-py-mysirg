'''
Recursion - I
'''


def printFirstNatural(n, endChar = '\n'):
  if n <= 0:
    return

  printFirstNatural(n - 1, endChar=' ')
  print(n, end=endChar)

def printFirstNaturalReverse(n):
  if n <= 0:
    return
  
  if n == 1:
    print(n)
  else:
    print(n, end=' ')
    printFirstNaturalReverse(n - 1)

def printFirstNaturalOdd(n, endChar = '\n'):
  if n <= 0:
    return

  printFirstNaturalOdd(n - 1, endChar=' ')
  print(n * 2 - 1, end=endChar)

def printFirstNaturalEven(n, endChar = '\n'):
  if n <= 0:
    return

  printFirstNaturalEven(n - 1, endChar=' ')
  print(n * 2, end=endChar)

def printFirstNaturalOddReverse(n):
  if n <= 0:
    return
  
  if n == 1:
    print(n)
  else:
    print(n * 2 - 1, end=' ')
    printFirstNaturalOddReverse(n - 1)

def printFirstNaturalEvenReverse(n):
  if n <= 0:
    return
  
  if n == 2:
    print(n)
  else:
    print(n * 2, end=' ')
    printFirstNaturalEvenReverse(n - 1)


def test():
  n = 10
  print('printFirstNatural')
  printFirstNatural(n)
  print('printFirstNaturalReverse')
  printFirstNaturalReverse(n)
  print('printFirstNaturalOdd')
  printFirstNaturalOdd(n)
  print('printFirstNaturalEven')
  printFirstNaturalEven(n)
  print('printFirstNaturalOddReverse')
  printFirstNaturalOddReverse(n)
  print('printFirstNaturalEvenReverse')
  printFirstNaturalEvenReverse(n)

test()
