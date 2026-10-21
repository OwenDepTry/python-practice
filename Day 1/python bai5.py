# Tìm số đầu tiên chia hết cho 9 và 7 trong khoảng [m,n]
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

if m > n:
    m, n = n, m

find = False

for i in range(m, n + 1):
    if i % 9 == 0 and i % 7 == 0:
        print("Số đầu tiên chia hết cho cả 9 và 7 là:", i)
        find = True
        break

if not find:
    print("Không có số thoả mãn")