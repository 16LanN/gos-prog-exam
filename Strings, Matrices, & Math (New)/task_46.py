# 46.	Calculate the Factorial of $N$.
n = 6
factorial = 1
for i in range(2, n+1):
    factorial *= i
print(factorial)