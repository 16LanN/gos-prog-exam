# 1.	Divide all elements of the array by the value of the largest element.
arr = [1, 4, 2, 6, 8, 9, 12, 5, 3, 7]
for i in arr:
    print(f'{i} / {max(arr)} = {i/max(arr)}')