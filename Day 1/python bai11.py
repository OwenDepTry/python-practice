# Quick sort giảm dần
def partition(a, left, right):
    pivot = a[right]
    i = left - 1

    for j in range(left, right):
        if a[j] > pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[right] = a[right], a[i + 1]

    return i + 1

def quick_sort(a, left, right):
    if left < right:
        pivot_pos = partition(a, left, right)

        quick_sort(a, left, pivot_pos - 1)
        quick_sort(a, pivot_pos + 1, right)


a = [8, 25, 32, 99, 1, 8, 7, 22]

quick_sort(a, 0, len(a) - 1)

print("Dãy giảm dần:", a)