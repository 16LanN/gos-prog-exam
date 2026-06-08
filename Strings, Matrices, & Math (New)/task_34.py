# 34.	Identify the first non-repeating character in a string.
string = 'vaeacuahuchsaeuhdxsavudhaymnz'
n = {}
for i in string:
    if i not in n:
        n[i] = 1
    elif i in n:
        n[i] += 1
for i in n:
    if n[i] == 1:
        print(i)
        break