# 18.	Count the total number of positive vs. negative elements separately.
arr = [1, -4, 2, 6, 8, -9, 12, 5, -3, 8, 7]
pos = 0
neg = 0
for i in arr:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
print(f'positive: {pos}, negative: {neg}')