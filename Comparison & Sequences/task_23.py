# 23.	Fill an array with random numbers within the interval $[a, b]$.
from random import randint
length = 7
arr = []
a = 3
b = 17
for i in range(length):
    c = randint(a, b)
    arr.append(c)
print(arr)