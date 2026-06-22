"""
2026/01/02
Source: University of Waterloo - CEMC Problem of the Week (POTW)
Gathering Treasure
Genevieve is making a video game where players need to trade gems in order to get to the next level.
The gems in the game are emeralds (💎), diamonds (◆), and rubies (●).
In the first level, players make three trades of their gems,
as shown in the diagram, until they have at least 10 rubies (●).
Start with 1 💎
Do you have at least 10 ●?
YES → You have finished the level
NO →
Trade 1 💎 for 2 ◆
Trade 2 ◆ for 3 ●
Trade 1 ● for 1 💎
(a) How many of each gem will a player have when they finish the first level?
(b) How many trades in total will a player have made when they finish this level?
"""
e=1
d=0
r=0
count=0
while r<10:
    if e>0:
        e=e-1
        d=d+2
        count = count + 1
    if d>1:
        d=d-2
        r=r+3
        count = count + 1
    if r>0:
        r=r-1
        e=e+1
        count = count + 1
print(f"emeralds are {e}, diamonds are {d}, rubies are {r}")  # question a
print(count) # question b


