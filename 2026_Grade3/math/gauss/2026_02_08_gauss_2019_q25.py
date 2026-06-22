"""
2026/02/08
Gauss 2019 Question 25
"""
s=0
for n in range(1200):
    if 12*n%(n+4) == 0:
        s=s+n
print(s)
