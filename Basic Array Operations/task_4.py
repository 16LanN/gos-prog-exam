# 4.	Find the minimum and maximum elements in an array and swap their positions.
arr = [42, -4, 2, 6, 8, -9, -12, 5, -3, 7]
mi = 0
ma = 0
for i in range(len(arr)):
    if arr[i] == min(arr):
        mi = i
    if arr[i] == max(arr):
        ma = i
arr[mi], arr[ma] = arr[ma], arr[mi]
print(arr)