"""
2026/01/13
https://dmoj.ca/problem/ccc08j1
"""
w=float(input())
h=float(input())
BMI=w/(h*h)
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<=25.0:
    print("Normal weight")
else:
    print("Overweight")