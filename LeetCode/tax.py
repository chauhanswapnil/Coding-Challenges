import itertools
import math 

def tax(N,X, Y, S):
  currentIndex = 0
  tax = 0
  while(currentIndex < N-1):
    currentValue = S[currentIndex]
    nextValue = S[currentIndex+1]
    if currentValue == '0' and nextValue == '1':
      tax += X
    if currentValue == '1' and nextValue == "0":
      tax += Y
    currentIndex += 1
  return tax

def calculateTaxBrute(N,X,Y,S):
  # Time Complexity
  # Exponential
  perm = list(itertools.permutations(S, N))
  minTax = math.inf
  for s in perm:
    t = tax(N, X, Y, s)
    if t < minTax:
      minTax = t
  return minTax

def calculateTax(N, X, Y, S):
  if("1" not in S):
    return 0

  if ("0" not in S):
    return 0

  if(X < Y):
    return X

  else:
    return Y

print(calculateTax(5, 5, 7, "11010"))
print(calculateTaxBrute(5, 5, 7, "11010"))

from Measure import measure
measure(calculateTax,11,5,7,"11010110101")
measure(calculateTaxBrute,11,5,7,"11010110101")


