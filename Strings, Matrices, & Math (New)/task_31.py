# 31.	Count the number of vowels in a given string.
vowels = "aeiouAEIOU"
counter = 0
string = 'something'
for i in string:
    if i in vowels:
        counter += 1
print(counter)