"""
Problem: Flight Duration
An airplane takes off at 0900 (9:00 AM) and lands at 1130 (11:30 AM).
Calculate the total duration of the flight in minutes.
Rules
Times are given in 24-hour format as four-digit integers (HHMM).
Use integer division (//) and modulus (%).
Do NOT use floating point division.
The landing time is guaranteed to be later on the same day.
 Input: Two integers:
0900
1130
Output
150
"""
st=int(input())
ed=int(input())
t1q=st//100*60
t1r=st%100
t2q=ed//100*60
t2r=ed%100
tt=(t2q+t2r)-(t1q+t1r)
print(tt)



