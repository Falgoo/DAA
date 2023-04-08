def divideGift(m, n, result):
    # Nếu chỉ có một học sinh thì gán tất cả các phần thưởng cho anh ta
    if n == 1:
        if m < result[-1]:
            return 0 # Trả về số cách chia là 0
        result.append(m)
        print(result)
        result.pop()
        return 1 
    else:
        count = 0 # Biến lưu số cách chia
        for i in range(1, m + 1):
            # Nếu số này lớn hơn hoặc bằng số cuối cùng trong kết quả
            if not result or i >= result[-1]:
                result.append(i)
                count += divideGift(m - i, n - 1, result)
                # Xóa số này khỏi kết quả để tiếp tục duyệt
                result.pop()
        return count

# Số phần thưởng 
m = 7
# Số học sinh 
n = 4
# Danh sách lưu kết quả
result = []
print("Các cách chia:")
total = divideGift(m, n, result)
print("Tổng số cách:", total)
