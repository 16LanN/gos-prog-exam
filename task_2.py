# 2.	Find the index and value of the first positive element in the array.
arr = [-1, -4, -2, 6, -8, 9, -12, 5, -3, 7]
index = 0
for i in arr:
    if i > 0:
        print(index, i)
        break
    index += 1