"""
2026/02/11
https://dmoj.ca/problem/ccc15j2
"""
r=input()
count1=0
count2=0
for i in range(len(r)-3):
    b=r[i:i+3]
    if b == ":-)":
        count1+=1
    elif b == ":-(":
        count2+=1
if count1==0 and count2==0:
    print("none")
elif count1 == count2:
    print("unsure")
elif count1 > count2:
    print("happy")
elif count1 < count2:
    print("sad")