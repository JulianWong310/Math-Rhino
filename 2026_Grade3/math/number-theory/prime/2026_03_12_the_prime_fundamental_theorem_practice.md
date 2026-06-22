# 🏆 Prime Bricks Detective (Updated)

---

**1. Which of the following numbers is a "Prime Brick" (a number that cannot be broken down into smaller integer factors other than 1 and itself)?**
* (A) 15
* (B) 21
* (C) 23
* (D) 25
* (E) 27

**2. If Number A has prime bricks [2, 2, 5] and Number B has prime bricks [2, 5, 5], what is their Greatest Common Divisor (GCD)?**
* (A) 2
* (B) 5
* (C) 10
* (D) 20
* (E) 50



**3. Using the "All-In Rule" (overlap the shared bricks), find the Least Common Multiple (LCM) of 12 and 18.**
*(Hint: $12 = 2 \times 2 \times 3$ and $18 = 2 \times 3 \times 3$)*
* (A) 6
* (B) 30
* (C) 36
* (D) 72
* (E) 216

**4. A number is a "Perfect Square" only if every prime brick in its recipe has a "twin brother" (even exponent). Which of the following is a perfect square?**
* (A) $2^3 \times 3^2$
* (B) $2^2 \times 5^1$
* (C) $2^4 \times 3^2$
* (D) $7^3$
* (E) $2 \times 3 \times 5$

**5. In Euclid's "Giant Tower" game, if our prime bag contains {2, 3, 5}, we build $N = (2 \times 3 \times 5) + 1 = 31$. Why does this prove there is a new prime?**
* (A) Because 31 is an even number.
* (B) Because 31 leaves a remainder of 1 when divided by 2, 3, or 5.
* (C) Because 30 is a prime number.
* (D) Because 31 is smaller than 30.
* (E) Because $31 = 3 \times 10 + 1$



**6. If the "Secret Recipe" of a mystery number is $2^3 \times 3^2 \times 5^1$, how many positive divisors does it have in total?**
*(Hint: Add 1 to each exponent and multiply them: $(3+1) \times (2+1) \times (1+1)$)*
* (A) 6
* (B) 12
* (C) 18
* (D) 24
* (E) 30

**7. What is the smallest number that is built from exactly three different prime bricks?**
* (A) 10
* (B) 15
* (C) 30
* (D) 42
* (E) 105

**8. If $(a, b)$ represents the GCD and $[a, b]$ represents the LCM, the "Magic Rule" says $(a, b) \times [a, b] = a \times b$. If $a=6$ and $b=10$, what is the result of $GCD \times LCM$?**
* (A) 16
* (B) 30
* (C) 60
* (D) 120
* (E) 2

**9. (New Recipe Rule) If a number $a = 2^3 \times 5^2$, which of the following CANNOT be a divisor of $a$?**
*(Hint: A divisor's bricks must be in the original pocket and have smaller or equal counts)*
* (A) $2^2 \times 5^1$
* (B) $2^0 \times 5^2$
* (C) $2^3 \times 5^3$
* (D) $2^1 \times 5^0$
* (E) $2^2 \times 5^2$

**10. If we add 1 to the product of the first four primes ($2 \times 3 \times 5 \times 7$), what is the remainder when the result is divided by 7?**
* (A) 0
* (B) 1
* (C) 2
* (D) 3
* (E) 6

---

## 🔑 Answer Key

1. **C** (23 has no factors other than 1 and 23)
2. **C** (Shared bricks: one 2 and one 5 $\rightarrow 10$)
3. **C** (Toolkit: [2, 2, 3, 3] $\rightarrow 36$)
4. **C** (Exponents 4 and 2 are both even)
5. **B** (It shows original primes can't be factors of the new number)
6. **D** ($4 \times 3 \times 2 = 24$)
7. **C** ($2 \times 3 \times 5 = 30$)
8. **C** ($6 \times 10 = 60$)
9. **C** (The original only has two [5]s, so it can't have a divisor with three [5]s)
10. **B** (Any "Tower + 1" divided by a tower brick leaves 1)