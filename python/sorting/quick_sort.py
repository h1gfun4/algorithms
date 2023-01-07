from datetime import datetime

items = [4, 1, 5, 3, 2]


# time complexity from 0(n log(n)) to 0(n^2)
# space complexity 0(log(n))
def quick_sort(data):
    def sort(s_data, fst, lst):
        if fst >= lst:
            return

        i, j = fst, lst
        x = s_data[(fst + lst) // 2]

        while i <= j:
            while s_data[i] < x:
                i += 1
            while s_data[j] > x:
                j -= 1
            if i <= j:
                s_data[i], s_data[j] = s_data[j], s_data[i]
                i, j = i + 1, j - 1
            sort(s_data, fst, j)
            sort(s_data, i, lst)
        return s_data

    return sort(list(data), 0, len(data) - 1)


sortItems = quick_sort(items)
# sortItems is [1, 2, 3, 4, 5]

print(items)
print(sortItems)

# simplified speed test
items = list(range(1, 200))
items[5], items[6] = items[6], items[5]
count = 1000
start = datetime.now()

for n in range(1, count):
    quick_sort(items)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(totalMicroseconds)
