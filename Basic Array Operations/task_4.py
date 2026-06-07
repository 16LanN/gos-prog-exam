# 4.	Find the minimum and maximum elements in an array and swap their positions.
arr = [42, -4, 2, 6, 8, -9, -12, 5, -3, 7]
mi = [0, False]
ma = [0, False]
for i in range(len(arr)):
    if arr[i] == min(arr):
        mi[0] = i
        mi[1] = True
    if arr[i] == max(arr):
        ma[0] = i
        ma[1] = True
    if ma[1] and mi[1]:
        break
arr[mi[0]], arr[ma[0]] = arr[ma[0]], arr[mi[0]]
print(arr)