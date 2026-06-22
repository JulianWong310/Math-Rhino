"""
2026/02/06
https://dmoj.ca/problem/ccc04j3
"""
n=int(input())
m=int(input())
lst1=[input().strip() for _ in range(n)]
lst2=[input().strip() for _ in range(m)]
for x in lst1:
    for y in lst2:
        print(f"{x} as {y}")