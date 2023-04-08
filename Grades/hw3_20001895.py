import time
import matplotlib.pyplot as plt
import numpy as np

def countTime(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start


def representBinary(x):
    if x == 0:
        return '0'
    elif x == 1:
        return '1'
    else:
        return representBinary(x//2) + str(x%2)

def printRepresentation():
    numbers = []
    times = []
    for i in range(1,10000):
        numbers.append(i)
        time = countTime(representBinary, i)
        times.append(time)
    plt.plot(numbers, times )
    plt.xlabel('n')
    plt.ylabel('Thời gian(s)')
    plt.title("Represention Binary Number")
    plt.show()

def analysis_prime_number(n, i = 2):
    if n < i:
      if n > 1:
        return [n]
      else:
        return []
    else:
      if n % i == 0:
        count = 0
        while n%i == 0:
            n //= i
            count += 1
        return [i]*count + analysis_prime_number(n , i + 1)
      else:
        return analysis_prime_number(n, i + 1)

def printAnalysisPrimeNumber():
    numbers = []
    times = []
    for i in range(1,900):
        numbers.append(i)
        time = countTime(analysis_prime_number, i)
        times.append(time)
    plt.plot(numbers, times )
    plt.xlabel('n')
    plt.ylabel('Thời gian(s)')
    plt.title("Analysis Prime Number")
    plt.show()


def findFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return findFibonacci(n-1) + findFibonacci(n-2)

def printFindFibonacci():
    numbers = []
    times = []
    for i in range(1,40):
        numbers.append(i)
        time = countTime(findFibonacci, i)
        times.append(time)
    plt.plot(numbers, times)
    plt.xlabel('n')
    plt.ylabel('Thời gian(s)')
    plt.title('Find Fibonacci')
    plt.show()

printFindFibonacci()

def towerOfHanoi(n,from_rod='a', to_rod='b', aux_rod='C'):
    if n == 1:
        return 1
    else:
        return towerOfHanoi(n-1,from_rod,aux_rod,to_rod) + towerOfHanoi(n-1,to_rod,from_rod,aux_rod) + 1

def printTowerOfHanoi():
    numbers = []
    times = []
    for i in range(1,30):
        numbers.append(i)
        time = countTime(towerOfHanoi, i)
        times.append(time)
    plt.plot(numbers, times)
    plt.xlabel('n')
    plt.ylabel('Thời gian(s)')
    plt.title('Tower Of Hanoi')
    plt.show()


def proceduce_bag(p,v,m):
    n = len(p)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    chosen = [[False for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if p[i-1] <=  j:
                if p[i-1] + dp[i-1][j-p[i-1]] > dp[i-1][j]:
                    dp[i][j] = v[i-1] + dp[i-1][j-p[i-1]]
                    chosen[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    i, j = n, M
    chosen_items = []
    while i > 0 and j > 0:
        if chosen[i][j]:
            chosen_items.append(i)
            j -= p[i-1]
        i -= 1
    chosen_items.reverse()
    return dp[n][M], chosen_items

def main():
    printRepresentation()
    printAnalysisPrimeNumber()
    printFindFibonacci()
    printTowerOfHanoi()
    
    M = 10
    P = [6,3,5,4,6]
    W = [2,2,6,5,4]
    a,b = proceduce_bag(P,W,M)
    print(a,b)
    
if __name__ == "__main__":
    main()
    
    
    

