# 39.	Perform a transpose on a $2 \times 2$ matrix.
matrix = [
    [1, 2],
    [3, 4]
]
matrix[0][1], matrix[1][0] = matrix[1][0], matrix[0][1]
print(matrix)