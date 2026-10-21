#Selection sort tăng dần
a = [8, 25, 32, 99, 1, 8, 7, 22]
n = len(a)

for i in range(n - 1):
    minpos = i

    for j in range(i + 1, n):
        if a[j] < a[minpos]:
            minpos = j

    a[i], a[minpos] = a[minpos], a[i]

print("Dãy tăng dần:", a)