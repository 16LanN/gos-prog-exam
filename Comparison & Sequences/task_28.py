# 28.	Sum the absolute values of all elements following the first negative number.
arr = [19812382198, -4, 2, 6, 8, -9, 12, 5, -3, 7]
trigger = False 
after_neg = []
for i in arr:
    if i < 0:
        trigger = True
    if trigger:
        after_neg.append(abs(i))
print(sum(after_neg))