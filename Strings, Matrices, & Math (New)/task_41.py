# 41.	Check if an array is sorted in non-descending order.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flag = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        flag = False
        break
print(flag)