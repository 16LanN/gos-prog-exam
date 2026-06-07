# 17.	Find the sum and count of elements within the interval $[a, b]$.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 8, 7]
a = 2
b = 9
count = 0
su = []
for i in arr:
    if i >= a and i <= b:
        count += 1
        su.append(i)
print(sum(su))
