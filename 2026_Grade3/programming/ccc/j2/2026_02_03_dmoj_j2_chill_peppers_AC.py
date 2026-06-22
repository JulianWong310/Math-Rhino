"""
2026/02/03
https://dmoj.ca/problem/ccc23j2
"""
n=int(input())
lst=[input().strip()for _ in range(n)]
count=0
for x in lst:
    if x == "Poblano":
        count+=1500
    elif x == "Mirasol":
        count+=6000
    elif x =="Serrano":
        count+=15500
    elif x =="Cayenne":
        count+=40000
    elif x =="Thai":
        count+=75000
    elif x =="Habanero":
        count+=125000
print(count)