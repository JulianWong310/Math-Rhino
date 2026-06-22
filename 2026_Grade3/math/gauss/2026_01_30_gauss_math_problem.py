"""
2026/01/30
Calculate the sum of all integers from 1 to 2017 that are not divisible by 2 and not divisible by 5.
"""
s=0
for i in range(1,2018):
    if i%2 and i%5:
        s+=i
print(s)