# 21.	Count elements that are strictly greater than both their immediate neighbors.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
counter = 0
for i in range(1, len(arr)-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        counter += 1
print(counter)