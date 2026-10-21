# In ra M SNT đầu tiên
def la_SNT(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

m = int(input("Nhập M: "))

if m <= 0:
    print("M phải là số nguyên dương")
else:
    count = 0
    num = 2

    while count < m:
        if la_SNT(num):
            print(num, end=" ")
            count += 1
        num += 1