# 9.	Calculate the sum of all positive elements.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 7]
su = []
for i in arr:
    if i > 0:
        su.append(i)
print(sum(su))