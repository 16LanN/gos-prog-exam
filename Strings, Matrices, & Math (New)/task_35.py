# 35.	Count the occurrences of a specific value $X$ in an array.
string = 'vaeacuahuchsaeuhdxsavudhaymnz'
n = {}
for i in string:
    if i not in n:
        n[i] = 1
    elif i in n:
        n[i] += 1
occurence = 'a'
print(n[occurence])