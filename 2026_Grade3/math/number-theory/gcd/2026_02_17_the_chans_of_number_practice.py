# 🎓 Number Clans
# Topic: Integer Math and Membership
# Date: February 17, 2026

# 1. The "Integer Only" Rule (Z)
# In CCC Junior problems, you are often told: "Input will be an integer n." 
# This means you must stay in the Integer Clan (Z).
# Problem: If you use /, Python moves you to the Float Clan (R).
# Trick: Always use // (Floor Division) to stay in the Integer Clan.
# Example: To find how many 3-pack juice boxes you can buy with 10 dollars, 
# use 10 // 3. The result is 3, not 3.333.

# 2. Using the Remainder (%)
# The Remainder is the most important tool for CCC.
# Even/Odd Check: n % 2
# If it is 0, it belongs to the Even Clan.
# If it is 1, it belongs to the Odd Clan.
# Digit Stripping: n % 10
# This always gives you the last digit of a number.

# 3. The "Belongs To" Check (isinstance)
# We sometimes need to check if a result is a "perfect" whole number.
# isinstance(x, int) is your "Security Guard." It checks if x belongs to Z.

# ✍️ Practice Challenge

# Q1. The Juice Box Problem
# A school needs to buy exactly n juice boxes. They come in packs of 6.
# Write a line of code to find how many full packs they can buy if they have 20 boxes.
# (Hint: Use the symbol for q from your cheat sheet).
print(20//6)

# Q2. The Last Digit Challenge
# If x = 1234, what code gives you the result 4?
x = 1234
print(x%10) # get 4

x1=x//10
print(x1%10) # get 3

# Q3. The Clan Guard
# Look at this logic:
x = 10 / 2
if isinstance(x, int):
    print("Q3 Answer: Clan Z")
else:
    print("Q3 Answer: Clan R")
# What will the computer print? Q3 Answer: Clan R
# (Hint: Remember Q1 from your notes—how does Python treat the / symbol?)

# Q4. Membership Proof
# A number is 'Perfect' if it is an Integer (Z).
# Which of these will jump out of the Integer Clan?
# 10 + 5
# 10 * 5
# 10 / 5  cto
# 10 // 5

# Run this in PyCharm to see the "Clan Jump" happen:

# 1. Start in Clan Z
a = 10
b = 3

# 2. Stay in Clan Z using //
result_int = a // b
print(f"Result {result_int} is Integer? {isinstance(result_int, int)}")

# 3. Jump to Clan R using /
result_float = a / b
print(f"Result {result_float} is Integer? {isinstance(result_float, float)}")



