# 6.	Find the sum of elements that are both even and negative.
arr = [1, -4, 2, 6, 8, -9, -12, 5, -3, 7, -2]
su = []
for i in range(len(arr)):
    if arr[i] % 2 == 0 and arr[i] < 0:
        su.append(arr[i])
print(sum(su))