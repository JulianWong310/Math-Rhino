"""
2026/01/22
Gauss Contest 2016 – Question 15
Sophia did push-ups every day for 7 days. Each day after the first day, she did 5 more
push-ups than the day before. In total she did 175 push-ups. How many push-ups
did Sophia do on the last day? justify the answer is 40.
"""
sum=0
x=10
for i in range(7):
    sum=sum+x
    x=x+5
print(f"last day: {x-5}")
print(f"total: {sum}")