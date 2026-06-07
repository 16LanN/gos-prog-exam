# 16.	Calculate both the sum and the product of all array elements.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 8, 7]
su = sum(arr)
mul = arr[0]
for i in range(1, len(arr)):
    mul *= arr[i]
print(su + mul)