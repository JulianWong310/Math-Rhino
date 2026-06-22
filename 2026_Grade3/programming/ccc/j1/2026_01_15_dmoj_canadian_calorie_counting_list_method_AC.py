"""
2026/01/15
https://dmoj.ca/problem/ccc06j1
"""
b=int(input())
s=int(input())
d=int(input())
e=int(input())

burger=[461,431,420,0]
side=[100,57,70,0]
drink=[130,160,118,0]
dessert=[167,266,75,0]

x= burger[b-1]+side[s-1]+drink[d-1]+dessert[e-1]

print(f"Your total Calorie count is {x}.")
