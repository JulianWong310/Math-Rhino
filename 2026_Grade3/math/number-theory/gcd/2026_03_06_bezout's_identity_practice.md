# 🏆 Bézout's Identity (Practice Set)

*Instructions: Choose the best answer for each question. These questions test your understanding of Bézout's Identity, GCD properties, and the "Bucket Logic".*

---

## 📝 Practice Questions

### 1. The Smallest Drop
If you have two measuring cups with capacities of **18 ml** and **42 ml**, what is the smallest positive amount of water (in ml) you can measure exactly?
* (A) 2  
* (B) 3  
* (C) 6  
* (D) 9  
* (E) 18

### 2. The Missing Multiple
A scientist has two chemical containers of size **$a$** and **$b$**. He knows that $\gcd(a, b) = 7$. Which of the following amounts is **IMPOSSIBLE** for him to measure?
* (A) 7  
* (B) 14  
* (C) 21  
* (D) 25  
* (E) 70

### 3. The Coprime Recipe
If $a$ and $b$ are **coprime** integers, which of the following equations MUST have an integer solution for $s$ and $t$?
* (A) $as + bt = 0$  
* (B) $as + bt = 1$  
* (C) $as + bt = \frac{1}{2}$  
* (D) $as + bt = a + b$  
* (E) Both (B) and (D)

### 4. Backtracking Logic
During the Subtraction Method for two numbers $x$ and $y$, the first step is $x - y = 5$ and the second step is $y - 5 = 2$. If the next step results in a remainder of 1, what is $\gcd(x, y)$?
* (A) 1  
* (B) 2  
* (C) 3  
* (D) 5  
* (E) 7

### 5. The Grid Jump
On an infinite number line, a robot can only jump **12 units** to the right or **15 units** to the left. What is the smallest positive coordinate the robot can land on if it starts at 0?
* (A) 1  
* (B) 3  
* (C) 5  
* (D) 12  
* (E) 15

### 6. Finding the Coefficients
If $\gcd(11, 3) = 1$, and we write the linear combination as $11s + 3t = 1$, which pair of $(s, t)$ works?
* (A) $(1, -3)$  
* (B) $(-1, 4)$  
* (C) $(2, -7)$  
* (D) $(1, -4)$  
* (E) $(-2, 8)$

### 7. The Large Bucket Mystery
Two large vats hold **$A$** and **$B$** gallons. If $A = 100$ and $B = 35$, the smallest non-zero amount we can measure is $d$. How many multiples of $d$ are there between 1 and 20 (inclusive)?
* (A) 2  
* (B) 3  
* (C) 4  
* (D) 5  
* (E) 6

### 8. Linear Combination Set
Let $S$ be the set of all integers that can be written as $14s + 21t$ for any integers $s, t$. Which of the following is true about $S$?
* (A) All elements in $S$ are even.  
* (B) All elements in $S$ are prime.  
* (C) All elements in $S$ are multiples of 7.  
* (D) $S$ only contains positive numbers.  
* (E) 1 is an element of $S$.

### 9. The Reversed Puzzle
If $d = \gcd(a, b)$ and $d = 3a - 4b$, which of the following must be true?
* (A) $d$ is a multiple of $a$.
* (B) $d$ is the smallest positive value in the form $sa + tb$.
* (C) $a$ must be an even number.
* (D) $b$ must be a prime number.
* (E) $d$ is always 1.

### 10. The Ultimate GCD Property
If $as + bt = 10$, which of the following values **CANNOT** be the $\gcd(a, b)$?
* (A) 1  
* (B) 2  
* (C) 5  
* (D) 10  
* (E) 20

---

## 🔑 Answer Key & Logic Analysis



| Q | Ans | Logic | Explanation |
| :--- | :--- | :--- | :--- |
| 1 | **(C)** | $\gcd(18, 42)$ | The smallest measurable amount is the GCD of 18 and 42, which is 6. |
| 2 | **(D)** | Multiples of $d$ | All measurable amounts must be multiples of 7. 25 is not a multiple of 7. |
| 3 | **(E)** | Bézout's Identity | If they are coprime, $\gcd=1$. We can make 1 (B) and any multiple of 1, including $a+b$ (D). |
| 4 | **(A)** | Subtraction Method | The GCD is the last non-zero remainder. If the process reaches 1, then $\gcd=1$. |
| 5 | **(B)** | $\gcd(12, 15)$ | The robot's jump "grid" is determined by $\gcd(12, 15) = 3$. |
| 6 | **(B)** | Backtracking | Test the pair: $11(-1) + 3(4) = -11 + 12 = 1$. It works. |
| 7 | **(C)** | Range Count | $\gcd(100, 35) = 5$. Multiples of 5 in the range [1, 20] are 5, 10, 15, and 20. |
| 8 | **(C)** | Multiple Rule | Since $\gcd(14, 21) = 7$, every linear combination must be a multiple of 7. |
| 9 | **(B)** | Minimal Property | Bézout's Identity states the GCD is the smallest positive integer of the form $sa+tb$. |
| 10 | **(E)** | Divisibility | The $\gcd(a, b)$ must be a divisor of the resulting sum (10). 20 is not a divisor of 10. |