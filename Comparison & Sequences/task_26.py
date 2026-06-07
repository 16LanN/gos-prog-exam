# 26.	Replace all elements at even-numbered indices with the value 999.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] = 999
print(arr)