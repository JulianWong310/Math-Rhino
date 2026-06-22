"""
2026-01-05
Draw a diamond (rhombus) pattern
      *
     ***
    *****
     ***
      *
"""
for i in range(1,6,2):
    star="*"*i
    space=" "*((5-i)//2)
    print(space+star+space)
for i in range(3,0,-2):
    star="*"*i
    space=" "*((5-i)//2)
    print(space+star+space)