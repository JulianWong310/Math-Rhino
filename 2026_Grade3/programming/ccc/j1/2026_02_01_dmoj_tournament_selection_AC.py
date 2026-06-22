"""
2026/02/01
https://dmoj.ca/problem/ccc16j1
"""

lst=[input().strip() for _ in range(6)]
count = 0
for x in lst:
    if x == "W":
        count+=1
if count == 5 or count == 6:
    print("1")
elif count == 3 or  count == 4:
    print("2")
elif count == 1 or count == 2:
  print("3")
else:
    print("-1")