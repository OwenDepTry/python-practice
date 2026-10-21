# Đếm chữ số và tính tổng các chữ số
n = int(input("Nhập một số nguyên: "))
num = abs(n)

count = 0
sum = 0

if num == 0:
    count = 1
else:
    while num > 0:
        digit = num % 10
        sum += digit
        count += 1
        num //= 10

print("Số chữ số:", count)
print("Tổng các chữ số:", sum)