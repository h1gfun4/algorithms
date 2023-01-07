from datetime import datetime


# time complexity 0(n log(n))
# space complexity 0(n)

def sort(data):
    result = []
    if len(data) < 2:
        return data
    l_left = len(data) // 2
    l_right = len(data) - l_left
    left = sort(data[:l_left])
    right = sort(data[l_left:])
    i = j = 0
    while i < l_left and j < l_right:
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result


items = [4, 1, 5, 3, 2]
sortItems = sort(items)
# sortItems is [1, 2, 3, 4, 5]

print(items)
print(sortItems)

# simplified speed test
items = list(range(1, 200))
items[5], items[6] = items[6], items[5]
count = 1000
start = datetime.now()

for n in range(1, count):
    sort(items)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds
print(totalMicroseconds)
