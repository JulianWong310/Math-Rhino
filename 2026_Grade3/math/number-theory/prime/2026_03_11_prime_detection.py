# Check if n is a prime number

import math
n=int(input())
limit = int(math.sqrt(n))
if n==1:
    print("It is not a prime number nor a composite number")
else:
    for i in range(2,limit+1):
        if n%i == 0:
            print("It is a composite number")
            break
    else:
        print("It is a prime number")
