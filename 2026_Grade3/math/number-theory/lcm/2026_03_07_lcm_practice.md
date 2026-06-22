# ✍️ GCD & LCM Connection: Comprehensive Practice

---

## 📝 Part 1: Basic Formulas & Logic

**1. If $gcd(a, b) = 10$ and $a \times b = 600$, what is $lcm(a, b)$?**
- (A) 6
- (B) 60
- (C) 600
- (D) 6000
- (E) 100

**2. Two numbers $x$ and $y$ are coprime. If $x \times y = 77$, what is $lcm(x, y)$?**
- (A) 1
- (B) 7
- (C) 11
- (D) 77
- (E) 154

**3. The $lcm(12, n) = 36$ and $gcd(12, n) = 6$. What is the value of $n$?**
- (A) 6
- (B) 12
- (C) 18
- (D) 24
- (E) 30

**4. For any two positive integers $a$ and $b$, what is the result of $(a \times b) \div lcm(a, b)$?**
- (A) 1
- (B) $gcd(a, b)$
- (C) $a + b$
- (D) $a - b$
- (E) $ab^2$

**5. If $a$ is a multiple of $b$, what is $gcd(a, b)$?**
- (A) 1
- (B) $a$
- (C) $b$
- (D) $a \times b$
- (E) 0



**6. The GCD of two numbers is 4 and their LCM is 48. If one number is 12, what is the other number?**
- (A) 4
- (B) 12
- (C) 16
- (D) 24
- (E) 48

**7. If $gcd(a, b) = a$, which of the following must be true?**
- (A) $b$ divides $a$
- (B) $a = b$
- (C) $a$ divides $b$
- (D) $a \times b = 1$
- (E) $lcm(a, b) = a$

**8. Find the LCM of $(2^3 \times 3^2)$ and $(2^2 \times 3^3)$.**
- (A) $2^2 \times 3^2$
- (B) $2^3 \times 3^3$
- (C) $2^5 \times 3^5$
- (D) 6
- (E) 12

**9. The product of two numbers is 120. If their GCD is 2, what is their LCM?**
- (A) 240
- (B) 120
- (C) 60
- (D) 30
- (E) 20

**10. Julian writes a Python function `lcm(a, b)`. If he inputs $a=14$ and $b=21$, what is the output?**
- (A) 7
- (B) 14
- (C) 21
- (D) 42
- (E) 294

---

## 📝 Part 2: The Property of LCM
*Theorem: Every common multiple of $a$ and $b$ is a multiple of their LCM.*

**11. If $lcm(a, b) = 12$, which of the following numbers CANNOT be a common multiple of $a$ and $b$?**
- (A) 12
- (B) 24
- (C) 36
- (D) 42
- (E) 60

**12. Suppose $M$ is a common multiple of $x$ and $y$. If $M$ is divided by $lcm(x, y)$, what must the remainder be?**
- (A) 0
- (B) 1
- (C) $gcd(x, y)$
- (D) It depends on $x$
- (E) It depends on $y$

**13. If $lcm(a, b) = 15$, and $M$ is a common multiple such that $40 < M < 50$, what is the value of $M$?**
- (A) 42
- (B) 44
- (C) 45
- (D) 48
- (E) 49

**14. If $lcm(a, b) = L$, and $k$ is a positive integer, is $k \cdot L$ always a common multiple of $a$ and $b$?**
- (A) Yes, always
- (B) No, only if $k$ is even
- (C) No, only if $k$ is prime
- (D) Only if $a=b$
- (E) Never

**15. Two numbers have a $gcd$ of 2 and an $lcm$ of 30. Which of the following is a possible common multiple of these two numbers?**
- (A) 15
- (B) 45
- (C) 75
- (D) 90
- (E) 100

---

## 📝 Part 3: The "Nested" LCM Rule (Associative Property)
*Theorem: $lcm(a_1, a_2, a_3) = lcm(lcm(a_1, a_2), a_3)$*

**16. To find the $lcm(4, 6, 10)$, Maya first calculates $lcm(4, 6) = 12$. What is her next step?**
- (A) $12 \times 10$
- (B) $lcm(12, 10)$
- (C) $gcd(12, 10)$
- (D) $4 + 6 + 10$
- (E) $lcm(4, 10)$

**17. If $lcm(a, b) = m$, what is the $lcm(a, b, m)$?**
- (A) $a \times b$
- (B) $m^2$
- (C) $m$
- (D) $1$
- (E) $a+b+m$

**18. Calculate $lcm(2, 3, 5)$ using the nested rule. What is the result?**
- (A) 10
- (B) 15
- (C) 30
- (D) 60
- (E) 1

**19. Given $lcm(10, 15) = 30$, find $lcm(10, 15, 20)$.**
- (A) 30
- (B) 40
- (C) 50
- (D) 60
- (E) 120

**20. A student claims that $lcm(a, b, c)$ is always equal to $a \times b \times c$. Under what condition is the "Nested Rule" result actually equal to the simple product $a \times b \times c$?**
- (A) When $a, b,$ and $c$ are all even.
- (B) When $a, b,$ and $c$ are pairwise coprime (share no common factors).
- (C) When $a$ is a multiple of $b$.
- (D) It is always equal.
- (E) It is never equal.



---

# 🔑 Answer Key

| Q | Ans | Reasoning |
| :--- | :--- | :--- |
| 1 | **B** | $600 \div 10 = 60$ |
| 2 | **D** | For coprime numbers, $lcm = x \times y$ |
| 3 | **C** | $n = (36 \times 6) \div 12 = 18$ |
| 4 | **B** | $(a \times b) \div lcm = gcd$ |
| 5 | **C** | If $b$ fits into $a$, $b$ is the greatest common divisor |
| 6 | **C** | $(4 \times 48) \div 12 = 16$ |
| 7 | **C** | If the GCD is $a$, then $a$ must be a factor of $b$ |
| 8 | **B** | Pick the highest power of each prime: $2^3$ and $3^3$ |
| 9 | **C** | $120 \div 2 = 60$ |
| 10 | **D** | Multiples of 14 (14, 28, 42...) and 21 (21, 42...) |
| 11 | **D** | 42 is not a multiple of 12 |
| 12 | **A** | The LCM divides all common multiples perfectly |
| 13 | **C** | 45 is the only multiple of 15 between 40 and 50 |
| 14 | **A** | Any multiple of the LCM is by definition a common multiple |
| 15 | **D** | 90 is a multiple of 30 ($30 \times 3$) |
| 16 | **B** | Nested rule: $lcm(Result1, NextNumber)$ |
| 17 | **C** | The LCM of a set and its own LCM is just the LCM |
| 18 | **C** | $lcm(2, 3) = 6$; then $lcm(6, 5) = 30$ |
| 19 | **D** | $lcm(30, 20) = 60$ |
| 20 | **B** | If they share no factors, no "overlap" is removed by the GCD |