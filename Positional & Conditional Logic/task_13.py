# 13.	Find the maximum absolute value among all elements ($|x|$).
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
a = 0
for i in arr:
    if abs(i) > a:
        a = abs(i)
print(a)