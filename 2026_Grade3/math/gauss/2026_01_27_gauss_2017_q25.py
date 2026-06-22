"""
2026/01/27
Gauss grade 7 2017 question 25
https://cemc.uwaterloo.ca/sites/default/files/documents/2024/2017Gauss7Contest.html
Ashley writes out the first 2017 positive integers.
She then underlines any of the 2017 integers that is a multiple of 2,
and then underlines any of the 2017 integers that is a multiple of 3,
and then underlines any of the 2017 integers that is a multiple of 5.
Finally, Ashley finds the sum of all the integers which have not been underlined.
 What is this sum?
"""
sm=0
for i in range(1,2018):
    if i%2!=0 and i%3!=0 and i%5!=0:
        sm+=i
print(sm)