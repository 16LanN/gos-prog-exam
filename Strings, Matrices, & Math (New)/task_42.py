# 42.	Implement a linear search to find the index of value $X$.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0
value = 4
for i in range(len(arr)):
    if arr[i] == value:
        index = i
        break
print(index)
