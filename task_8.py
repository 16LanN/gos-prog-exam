# 8.	Identify elements greater than the arithmetic average of the entire array.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
greater = []
for i in arr:
    if i > (sum(arr)/len(arr)):
        greater.append(i)
print(greater)