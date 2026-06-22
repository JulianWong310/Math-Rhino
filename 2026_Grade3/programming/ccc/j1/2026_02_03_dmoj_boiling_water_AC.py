"""
2026/02/03
https://dmoj.ca/problem/ccc21j1
"""
B=int(input())
p=5*B-400
print(p)
if p>100:
    print("-1")
elif p<100:
    print("1")
else:
    print("0")
