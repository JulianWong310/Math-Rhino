"""
2026/01/17
https://dmoj.ca/problem/ccc11j1
"""
a=int(input())
e=int(input())
if a>2 and e<5:
    print("TroyMartian")
if a<7 and e>1:
    print("VladSaturnian")
if a<3 and e<5:
    print("GraemeMercurian")
else:
    print()