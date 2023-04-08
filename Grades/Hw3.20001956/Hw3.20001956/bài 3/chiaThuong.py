def count_award(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    elif m < n:
        return count_award(m, m)
    else:
        return count_award(m - n, n) + count_award(m, n - 1)

m = int(input("Nhap so phan thuong: "))
n = int(input("Nhap so hoc sinh gioi: "))
result = count_award(m, n)
print("So cach chia phan thuong la:", result)
