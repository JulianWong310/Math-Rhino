"""
2026/02/04
https://dmoj.ca/problem/ccc18j1
"""
lst=[int(input())for _ in range(4)]
if (lst[0] == 8 or lst[0] == 9) and (lst[3] == 8 or lst[3] == 9) and lst[1] == lst[2]:
    print("ignore")
else:
    print("answer")