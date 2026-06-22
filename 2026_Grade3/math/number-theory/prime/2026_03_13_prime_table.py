# print all the prime numbers from 1-1000
import math
for i in range(2,1001): # 2, 3, 4, 5
    limit=int(math.sqrt(i)) # 1, 1, 2 , 2
    for j in range(2, limit+1): # (2,2), (2,2), (2,3),(2,3)
        if i % j == 0: # 4%2
            break
    else:
       print(i) # 2, 3,5

