"""
2026/01/18
https://dmoj.ca/problem/ccc02j1
"""
a=int(input())
def s1():
    print(" * * *")
def s2():
    for i in range (3):
        print("*")
def s3():
    for i in range(3):
        print("      *")
def s4():
    for i in range(3):
        print("*     *")

if a==0:
    s1()
    s4()
    print()
    s4()
    s1()
elif a==1:
    print()
    s3()
    print()
    s3()
    print()
elif a==2:
    s1()
    s3()
    s1()
    s2()
    s1()
elif a ==3:
    s1()
    s3()
    s1()
    s3()
    s1()
elif a==4:
    print()
    s4()
    s1()
    s3()
    print()
elif a==5:
    s1()
    s2()
    s1()
    s3()
    s1()
elif a==6:
    s1()
    s2()
    s1()
    s4()
    s1()
elif a==7:
    s1()
    s3()
    print()
    s3()
    print()
elif a==8:
    s1()
    s4()
    s1()
    s4()
    s1()
elif a==9:
    s1()
    s4()
    s1()
    s3()
    s1()