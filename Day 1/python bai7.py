# Tính giai thừa bằng đệ quy
# Công thức: n! = n x (n - 1)!, với 0! = 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input("Nhập một số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương")
else:
    print(f"{n}! = {factorial(n)}")