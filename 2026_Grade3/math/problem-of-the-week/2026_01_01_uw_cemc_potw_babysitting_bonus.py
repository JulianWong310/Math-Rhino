"""
2026/01/01
Source: University of Waterloo - CEMC Problem of the Week (POTW)
Babysitting Bonus
Anya agrees to look after her younger brother every day for 1 hour before dinner.
Her parents agree to pay her $15 per week, starting in September.
If Anya does a spectacular job, her parents will give her a raise of $2 per week,
beginning on the first Monday of each new month.
So far, Anya has done a spectacular job.
Anya’s parents have a monthly household budget.
They want to estimate how much they will be spending on babysitting each month.
Question
Determine the first month in which Anya’s estimated babysitting earnings are more than $100.
You may assume that there are 4 weeks in each month.
"""
count=0
w=15
while w*4<=100:
    w=w+2
    count=count+1
print(w*4)
print(count) # 6 months after September
# Therefore the first month is March.