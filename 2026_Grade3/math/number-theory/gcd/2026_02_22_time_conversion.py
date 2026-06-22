"""
2026/2/22
Time Conversion
"""
"""
Problem 1: Minutes Conversion
You are given a non-negative integer T, representing a number of seconds.
Convert this time into:
MM:SS
Input
A single integer:
T
0 ≤ T ≤ 100000
Output
Print the time in format:
MM:SS
Both values must be two digits.
Example
Input:
125
Output:
02:05
"""
t=int(input())
mm=t//60
ss=t%60
print(f"{mm:02}:{ss:02}")

"""
Problem 2: Second Conversion
You are given a non-negative integer 3671, representing a number of seconds.
Convert this time into hours, minutes, and seconds, and print it in the format:
HH:MM:SS
📌 Rules
Use integer division (//) and modulus (%)
All values must be integers
Hours, minutes, and seconds must be printed using two digits
Use 02d for formatting
Do NOT use floating point division
"""
# 📤🐍
t=3671
hh=t//3600
mm=t%3600//60
ss=t%60
print(f"{hh:02d}:{mm:02d}:{ss:02d}")

"""
Problem 3: Back to Clock Time
You are given a non-negative integer M, representing the number of minutes that have passed since midnight (00:00).
Convert this value into 24-hour clock format and print the time as a four-digit integer HHMM.
Rules
0 ≤ M < 1440
Use integer division (//) and modulus (%)
Do NOT use floating point division
Hours and minutes must always be two digits
Output must be printed as a four-digit number (leading zeros required)
Input
A single integer:
M
Output
Print the time in 24-hour format:
HHMM
Example 1
Input
90
Output
0130
Explanation
90 // 60 = 1 hour
90 % 60 = 30 minutes
So the time is 01:30 → printed as 0130.
Example 2
Input
780
Output
1300
Explanation
780 // 60 = 13 hours
780 % 60 = 0 minutes
So the time is 13:00 → printed as 1300.
"""
t=int(input())
hh=t//60
mm=t%60
print(f"{hh:02}{mm:02}")

"""
Problem 4: Total Minutes Since Midnight
You are given a time in 24-hour format as a four-digit integer.
Convert it into the total number of minutes since midnight.
Input
A single integer:
HHMM
0000 ≤ HHMM ≤ 2359
Minutes are valid (00–59)
Output
Print a single integer representing total minutes since 00:00.
Example
Input:
1300
Output:
780
Explanation:
13 × 60 = 780
"""
t=int(input())
hh=t//100
mm=t%100
tt=hh*60+mm
print(tt)