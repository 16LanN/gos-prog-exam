# 37.	Extract and print the elements of the main diagonal of a matrix.
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
extract = []
for i in range(len(matrix)):
    extract.append(matrix[i][i])
print(extract)