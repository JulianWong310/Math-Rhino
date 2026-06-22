"""
2026/02/08
Gauss 2019 Question 24
"""

steps1 = [1, 3, 5, 7, 9]
steps2 = [2, 4, 6, 8, 10]
x = [20]
y = [19]

# case 1 first move x, then move y
for i in steps1:                   # i=1, 3
    new_results = []
    for j in x:                    # j=20, 21/19,
        new_results.append(j+i)    # [21], [24,22]
        new_results.append(j-i)    # [21,19],[24,18,22,16]
    x = new_results                # [21,19],[24,18,22,16]
print(x)
for n in steps2:
    new_result2=[]
    for t in y:
        new_result2.append(t+n)
        new_result2.append(t-n)
    y = new_result2
print(y)

# case 2 first move y, then move x
x2=[20]
y2=[19]
for i in steps2:
    new_results = []
    for j in x2:
        new_results.append(j+i)
        new_results.append(j-i)
    x2 = new_results
print(x2)
for n in steps1:
    new_result2=[]
    for t in y2:
        new_result2.append(t+n)
        new_result2.append(t-n)
    y2 = new_result2
print(y2)

if 30 in x and 40 in y or 30 in x2 and 40 in y2:
    print("yes")
else:
    print("No")