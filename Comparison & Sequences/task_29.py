# 29.	Calculate the product of all elements appearing before the first negative number.
arr = [1, 4, 2, 6, -8, -9, 12, 5, -3, 7]
product = arr[0]
for i in range(1, len(arr)):
    if arr[i] < 0:
        break
    product *= arr[i]
print(product)
