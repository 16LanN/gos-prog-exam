# 12.	Find indices of elements that fall within the range $[X, Y]$.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
x = 5
y = 11
new = []
for i in arr:
    if i >= x and i <= y:
        new.append(i)
print(new)