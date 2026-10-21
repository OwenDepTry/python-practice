# Đảo ngược chuỗi
string = input("Nhập một chuỗi: ")
reverse = ""

for char in string:
    reverse = char + reverse

print("Chuỗi đảo ngược:", reverse)

# Cách viết bằng Slicing
string = input("Nhập một chuỗi: ")
print("Chuỗi đảo ngược:", string[::-1])