"""
2026/01/10
Gigi's Square Tiles
https://dmoj.ca/problem/ccc04j1
Gigi has many small square tiles. She wants to make one big square.
* A square has the same length and width.
* Area = Length × Length.
If she has 8 tiles, the biggest square she can make is 2 × 2 (Area 4).
She can't make 3 × 3 because she would need 9 tiles.
Your task:
Input the number of tiles and find the largest side length.

Sample Input 1
9
Sample Output 1
The largest square has side length 3.

Sample Input 2
8
Sample Output 2
The largest square has side length 2.

Sample Input 3
7535
Sample Output 3
The largest square has side length 86.
"""
n=int(input())
side=1
while side*side<=n:
    side=side+1
print(f"The largest square has side length {side-1}.")