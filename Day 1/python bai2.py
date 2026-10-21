# Liệt kê các snt nhỏ hơn N
def la_SNT(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input("Nhập N: "))

print("Các số nguyên tố nhỏ hơn", n, "là: ")
for i in range(2, n):
    if la_SNT(i):
        print(i, end=" ")