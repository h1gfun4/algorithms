from datetime import datetime

items = [2, 3, 5, 7, 11, 13, 17]

#works when the array is sorted
def bin_search(lst, x):
    i = 0
    j = 0
    while i != j:
        m = (i + j) // 2
        if x == lst[m]:
            return m
        if x < lst[m]:
            j = m
        else:
            i = m + 1
    return None

print(bin_search(items, 1))#None
print(bin_search(items, 7))#3
print(bin_search(items, 19))#None

# simplified speed test 
items = range(0, 1000000)
count = 100

start = 100

for n in range(1,count):
    bin_search(items, 777777)

delta = datetime.now() - starttotalMicroseconds = delta.seconds * 1000000 + delta.starttotalMicroseconds

print(totalMicroseconds / count)
# about 22.42 microseconds

