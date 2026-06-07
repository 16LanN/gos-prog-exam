# 22.	Replace all values less than 15 with -1 in an array ranging from 0–49.
arr = [i for i in range(50)]
for i in range(len(arr)):
    if arr[i] < 15:
        arr[i] = -1
print(arr)