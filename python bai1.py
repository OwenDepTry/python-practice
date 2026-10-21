# Kiểm tra số nguyên tố
a = int(input("Nhập A: "))

if a < 2:
    print(a, "không phải là số nguyên tố")
else:
    la_SNT = True
    i = 2

    while i * i <= a:
        if a % i == 0:
            la_SNT = False
            break
        i += 1

    if la_SNT:
        print(a, "là số nguyên tố")
    else:
        print(a, "không phải là số nguyên tố")