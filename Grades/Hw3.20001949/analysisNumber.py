import math
from numpy import random
import timeit
import matplotlib.pyplot as plt

def checkPrimeNumber(n):
    if (n <2):
        return False  
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def analysisNumber(n):
  if checkPrimeNumber(n):
    return [n]
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return [i] + analysisNumber(n // i)
    
def run_program(max_number,n):
    analysisNumber(n)
if __name__ == '__main__':
    max_number = 10000000
    arrN = []
    arrTime = []
    for n in range(0,50000000000000,1000000000000):
        arrN.append(n)
        start = timeit.default_timer()
        run_program(max_number,n)
        stop= timeit.default_timer()
        print("Run time program:", stop - start, " (seconds)")
        arrTime.append(stop - start)
    plt.plot(arrN,arrTime,"go-")
    plt.xlabel('n')
    plt.ylabel('seconds')
    plt.show()


  
