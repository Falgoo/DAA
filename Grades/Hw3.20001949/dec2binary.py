from numpy import random
import timeit
import matplotlib.pyplot as plt
def dec2binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2 + 10 * dec2binary(int(n // 2)))
    
def run_program(max_number,n):
    dec2binary(n)
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

