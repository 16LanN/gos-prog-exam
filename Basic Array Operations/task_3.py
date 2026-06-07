# 3.	Replace all elements in an array with their opposite signs (e.g., $1 \rightarrow -1$).
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
for i in range(len(arr)):
    arr[i] = arr[i]-arr[i]*2
print(arr)