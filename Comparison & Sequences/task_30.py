# 30.	Find the sum of elements located between the min and max (excluding min/max).
arr = [1, -7, 2, 6, 8, -2, 12, 5, -3, 7]
mi = 0
ma = 0
for i in range(len(arr)):
    if arr[i] == min(arr):
        mi = i
    if arr[i] == max(arr):
        ma = i
endpoints = sorted([ma, mi])
sums = []
for i in range(len(arr)):
    if endpoints[0] < i and endpoints[1] > i:
        sums.append(arr[i])
print(sum(sums))