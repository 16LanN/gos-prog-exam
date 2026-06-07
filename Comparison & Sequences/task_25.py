# 25.	Calculate the sum of elements located between two zeros.
arr = [-1231231, -434533, 0, 6, 5, -9, 12, 8, -3, 0, 123, 453]
flag_zero = False
new = []
first_zero = 0
for i in range(len(arr)):
    if arr[i] == 0:
        flag_zero = True
        first_zero = i
    if flag_zero:
        new.append(arr[i])
        if i != first_zero and arr[i] == 0:
            flag_zero = False
print(sum(new))