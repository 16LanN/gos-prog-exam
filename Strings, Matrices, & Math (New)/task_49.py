# 49.	Find the sum of the individual digits of an integer.
n = 493
nums = []
for i in str(n):
    nums.append(int(i))
print(sum(nums))