from numpy import random
import timeit
import matplotlib.pyplot as plt
def MoveTower(n,A,B,C):
    if (n==1):
        Move1Dick(A,B)
    else:
        MoveTower(n-1,A,C,B)
        Move1Dick(A,B)
        MoveTower(n-1,C,B,A)
def Move1Dick(A,B):
    print(A," -> ",B)
    
def run_program(max_number,n):
    MoveTower(n,"A","B","C")
if __name__ == '__main__':
    max_number = 10000000
    arrN = []
    arrTime = []
    for n in range(1,21,5):
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

