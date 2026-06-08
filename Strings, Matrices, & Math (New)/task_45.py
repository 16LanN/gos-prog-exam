# 45.	Create a frequency map (dictionary) of all elements in an array.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7, 7, -4, 1, 8, 5, 7, 4, 5, 123, 32, 2, 3, 7, 7, 9]
d = {}
for i in range(len(arr)):
    if str(arr[i]) not in d:
        d[str(arr[i])] = 1
    else:
        d[str(arr[i])] += 1
print(d)