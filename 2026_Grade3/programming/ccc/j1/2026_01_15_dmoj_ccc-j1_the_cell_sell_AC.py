"""
2026/01/15
https://dmoj.ca/problem/ccc05j1
"""
a= int(input())
b= int(input())
c= int(input())
et=b*15
wt=c*20
if a > 100:
    dt=(a-100)*25
else:
    dt=0
xa=(dt+et+wt)/100
print(f"Plan A costs {xa}")

etb=b*35
wtb=c*25
if a> 250:
    dtb=(a-250)*45
else:
    dtb=0
xb=(dtb+etb+wtb)/100
print(f"Plan B costs {xb}")

if xa<xb:
    print("Plan A is cheapest.")
elif xa>xb:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")


