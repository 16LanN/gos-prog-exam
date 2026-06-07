# 19.	Find the maximum of all negative elements and swap it with the last element.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 8, 7]
lowest_index = 0
l = arr[0]
for i in range(1, len(arr)):
    if arr[i] < l:
        l = arr[i]
        lowest_index = i
arr[lowest_index], arr[-1] = arr[-1], arr[lowest_index]
print(arr)