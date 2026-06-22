"""
2026/02/12
https://dmoj.ca/problem/ccc01j2
"""
x=int(input())
m=int(input())
for n in range(1,m):
    if x*n%m == 1:
        print(n)
        break
else:
    print("No such integer exists")