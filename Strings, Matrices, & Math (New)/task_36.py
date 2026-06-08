# 36.	Calculate the total sum of all elements in a 2D Matrix.
nums = [[1,2,3], [4,5,6], [7,8,9]]
summa = 0
for i in nums:
    summa += sum(i)
print(summa)