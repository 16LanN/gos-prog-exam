# 24.	Find the sum of the indices of the minimum and maximum elements.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
mi = 0
ma = 0
for i in range(len(arr)):
    if arr[i] == max(arr):
        ma = i
    if arr[i] == min(arr):
        mi = i
print(mi + ma)