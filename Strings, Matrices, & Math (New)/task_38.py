# 38.	Find the index of the row with the highest sum in a matrix.
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [21, 22, 23, 24, 25],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]
sums = []
for i in matrix:
    sums.append(sum(i))
for i in range(len(sums)):
    if sums[i] == max(sums):
        print(i)
        break 