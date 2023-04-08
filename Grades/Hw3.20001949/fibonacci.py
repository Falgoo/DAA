from numpy import random
import timeit
import matplotlib.pyplot as plt

def fibonacci(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def run_program(max_number,n):
        fibonacci(n)

if __name__ == '__main__':
    max_number = 10000000
    arrN = []
    arrTime = []
    for n in range(10,50,5):
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



