# 15.	Compare the sum of elements from index $0$ to $K$ vs. $K+1$ to the end.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 8, 7]
k = 6
before = []
after = []
for i in range(len(arr)):
    if i <= k:
        before.append(arr[i])
    elif i > k:
        after.append(arr[i])
if sum(before) > sum(after):
    print('before')
elif sum(before) < sum(after):
    print('after')
else:
    print('even')