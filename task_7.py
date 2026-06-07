# 7.	Find the minimum value among elements located at odd indices ($1, 3, 5, \dots$).
arr = [1, -4, 2, 6, 8, -9, -12, 5, -3, 7]
mi = []
for i in range(len(arr)):
    if i % 2 == 1:
        mi.append(arr[i])
print(min(mi))