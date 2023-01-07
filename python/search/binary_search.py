from datetime import datetime, time

items = [2, 3, 5, 7, 11, 13, 17]


def bin_search(lst, item):
    low = 0
    high = len(lst) - 1
    i = 0
    while low <= high:
        mid = (low + high) // 2
        if item == lst[mid]:
            return mid
        if item < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
        i = i + 1
    return None


print(bin_search(items, 1))  # None
print(bin_search(items, 7))  # 3
print(bin_search(items, 19))  # None

items = list(range(0, 1000000))
r_count = 100

start = datetime.now()

for n in range(1, r_count):
    bin_search(items, 777777)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(totalMicroseconds / r_count)
