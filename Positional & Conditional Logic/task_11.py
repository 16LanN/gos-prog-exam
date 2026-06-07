# 11.	Replace the minimum element with the arithmetic average of the array.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
m = 0
a = min(arr)
for i in range(len(arr)):
    if a == arr[i]:
        m = i
        break
arr[m] = (sum(arr)/len(arr))
print(arr)