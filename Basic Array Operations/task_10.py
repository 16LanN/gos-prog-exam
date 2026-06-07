# 10.	Count the total number of positive elements.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
counter = 0
for i in arr:
    if i > 0:
        counter += 1
print(counter)