# 14.	Find the average of even elements located at odd indices.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 8, 7]
avg = []
for i in range(len(arr)):
    if arr[i] % 2 == 0 and i % 2 == 1:
        avg.append(arr[i])
print(sum(avg)/len(avg))