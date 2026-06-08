# 47.	Generate the first $N$ numbers of the Fibonacci sequence.
n = 7
fib = [0, 1]
for i in range(0, n-2):
    fib_new = fib[i] + fib[i+1]
    fib.append(fib_new)
print(fib[:n])