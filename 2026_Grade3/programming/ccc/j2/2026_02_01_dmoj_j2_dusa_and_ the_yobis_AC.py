"""
2026/02/01
https://dmoj.ca/problem/ccc24j2
"""
d= int(input())
while True:
    y=int(input())
    if d>y:
        d+=y
    else:
        break
print(d)