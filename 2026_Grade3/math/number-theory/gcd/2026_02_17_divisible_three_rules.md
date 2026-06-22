# 🧮 Euclidean Rules
**Topic:** Divisibility & The Euclidean Rules
**Date:** February 17, 2026

---

## 1. What is "Divisibility"?
In Python, we use `%` to find remainders. In Number Theory, we look for cases where the **Remainder is ZERO**.

* **Definition:** We say $b$ divides $a$ (written as **$b|a$**) if there is some integer $q$ such that:
  > $$a = b \cdot q$$
* **In English:** $b$ is a **factor** of $a$, and $a$ is a **multiple** of $b$.
* **Python Check:** `if a % b == 0:` (This means $b$ divides $a$ perfectly).

---

## 2. The Three Golden Rules (Theorems)

Mathematicians use these "rules" to solve big puzzles without doing long division.

### Rule 1: The Chain Rule (Transitivity)
If a small number divides a middle number, and the middle number divides a big number, then the small one divides the big one too!
* **Logic:** If $a|b$ and $b|c$, then **$a|c$**.
* **Example:** $2|10$ and $10|100$ $\rightarrow$ Therefore, $2|100$.

### Rule 2: The Addition/Subtraction Rule
If a number $m$ divides two different numbers, it also divides their sum and their difference.
* **Logic:** If $m|a$ and $m|b$, then **$m|(a + b)$** and **$m|(a - b)$**.
* **Example:** $5|10$ and $5|25$. Since this is true, 5 must also divide $35$ ($10+25$) and $15$ ($25-10$).

### Rule 3: The Combo Rule (Linear Combination)
This is the "Super Power" version of Rule 2. If $m$ divides $a$ and $b$, it divides any "combo" of them (like $2a + 3b$).
* **Logic:** If $m|a$ and $m|b$, then **$m|(qa + rb)$** for any integers $q$ and $r$.
* **Coding Thought:** This is like creating a function `combo(a, b)` where the result is always divisible by $m$.

---

## ✍️ Practice Challenges 

**Q1. The Python Modulo Test**
Which of these would return `True` in Python? (Remember: $b|a$ means `a % b == 0`)
* A) $3 | 12$
* B) $5 | 21$
* C) $7 | 0$

**Q2. The Chain Rule Mystery**
If $x | 8$ and $8 | 64$, does $x$ have to divide $64$? Why?

**Q3. The Secret Addition**
Without using a calculator: If $13 | 130$ and $13 | 26$, does $13$ divide $156$? 
*(Hint: $156 = 130 + 26$. Use Rule 2!)*

**Q4. The Combo Challenge**
If $m$ is a factor of both $10$ and $4$, does $m$ have to be a factor of $2$?
*(Hint: Use Rule 2 for subtraction: $10 - 4 - 4 = 2$)*

---
