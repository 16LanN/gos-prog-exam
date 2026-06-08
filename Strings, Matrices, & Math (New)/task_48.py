# 48.	Check if a number $N$ is a Prime number.
n = 19
flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
        break
print(flag)