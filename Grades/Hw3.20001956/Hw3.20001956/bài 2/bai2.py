import time
import matplotlib.pyplot as plt

def decimal_to_binary(decimal):
    if decimal > 1:
        decimal_to_binary(decimal // 2)
    print(decimal % 2, end='')

number = int(input("Nhập số nguyên: "))
decimal_to_binary(number)


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
n = int(input("\nNhập số nguyên: "))
print("Thừa số nguyên tố của", n, "là:", prime_factors(n))


n_values = []
times = []

for n in range(10, 10001, 100):
    start_time = time.time()
    prime_factors(n)
    end_time = time.time()
    n_values.append(n)
    times.append(end_time - start_time)

plt.plot(n_values, times)
plt.title('Biểu đồ tăng trưởng thời gian')
plt.xlabel('Giá trị đầu vào (n)')
plt.ylabel('Thời gian thực hiện (giây)')
plt.show()