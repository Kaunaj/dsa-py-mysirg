'''
Recursion - II
'''

def sumFirstNatural(n):
  if n == 1:
    return n
  else:
    return n + sumFirstNatural(n - 1)

def sumFirstNaturalOdd(n):
  if n == 1:
    return n
  else:
    return (n * 2 - 1) + sumFirstNaturalOdd(n - 1)

def sumFirstNaturalEven(n):
  if n == 0:
    return n
  else:
    return (n * 2) + sumFirstNaturalEven(n - 1)

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

def sumOfSquaresFirstNatural(n):
  if n == 1:
    return n
  else:
    return n**2 + sumOfSquaresFirstNatural(n - 1)


def test():
  n = 10
  print(f'sum of first {n} natural numbers: {sumFirstNatural(n)}')
  print(f'sum of first {n} odd natural numbers: {sumFirstNaturalOdd(n)}')
  print(f'sum of first {n} even natural numbers: {sumFirstNaturalEven(n)}')
  print(f'factorial of {n}: {factorial(n)}')
  print(f'sum of squares of first {n} natural numbers: {sumOfSquaresFirstNatural(n)}')
  
test()
