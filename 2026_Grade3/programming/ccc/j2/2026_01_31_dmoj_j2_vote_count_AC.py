"""
2026/01/31
https://dmoj.ca/problem/ccc14j2
"""
v=int(input())
l=input().strip()
acount=0
bcount=0
for x in l:
    if x == "A":
        acount+=1
    elif x == "B":
        bcount+=1
if bcount<acount:
    print("A")
elif acount<bcount:
    print("B")
else:
    print("Tie")