# 20.	Count how many elements' absolute values are greater than the array's maximum.
arr = [1, -4, 2, 6, 8, -9, 5, -3, 8, 7, -13, -16, -10]
counter = 0
for i in arr:
    if abs(i) > max(arr):
        counter += 1
print(counter)