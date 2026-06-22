"""
2026/01/15
https://dmoj.ca/problem/ccc06j1
"""
b=int(input())
s=int(input())
d=int(input())
e=int(input())

def br():
    if b==1:
        return 461
    elif b==2:
        return 431
    elif b==3:
        return 420
    elif b==4:
        return 0
def se():
    if s==1:
        return 100
    elif s==2:
        return 57
    elif s==3:
        return 70
    elif s==4:
        return 0
def dk():
    if d==1:
        return 130
    elif d==2:
        return 160
    elif d==3:
        return 118
    elif d==4:
        return 0

def dt ():
    if e==1:
        return 167
    elif e==2:
        return 266
    elif e==3:
        return 75
    elif e==4:
        return 0
x=br()+se()+dk()+dt()
print(f"Your total Calorie count is {x}.")
