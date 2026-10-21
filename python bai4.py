# In các số chẵn trong khoảng (m,n)
m = int(input("Nhập M: "))
n = int(input("Nhập N: "))

if m > n:
    m, n = n, m

print("Các số chẵn trong khoảng là: ")
for i in range(m+1, n):
    if i % 2 == 0:
        print(i, end=" ")