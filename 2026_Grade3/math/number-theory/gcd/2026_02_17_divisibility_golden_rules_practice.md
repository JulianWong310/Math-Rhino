# 🏆 Divisibility Challenges
**Topic:** The Three Golden Rules of Divisibility  
**Target:** AMC 8 / Grade 3-5 Competitive Math  
**Clans involved:** $\mathbb{Z}$ (Integers) and $\mathbb{N}$ (Natural Numbers)

---

### 📜 The Rules Refresher
1.  **Rule 1 (Transitivity):** If $a|b$ and $b|c$, then $a|c$.
2.  **Rule 2 (Add/Sub):** If $m|a$ and $m|b$, then $m|(a+b)$ and $m|(a-b)$.
3.  **Rule 3 (Combo):** If $m|a$ and $m|b$, then $m|(qa + rb)$ for any integers $q, r$.

---

### 📝 Part 1: The Chain Rule (Transitivity)

**Q1.** If $3$ divides $n$ and $n$ divides $30$, which of the following is **NOT** a possible value for $n$?
* (A) 3
* (B) 6
* (C) 10
* (D) 15

**Q2.** If $a \mid b$ and $b \mid c$, and we know $a=5$ and $c=20$, which value could $b$ be?
* (A) 2
* (B) 10
* (C) 15
* (D) 25

---

### 📝 Part 2: The Addition & Subtraction Rules

**Q3.** If $m \mid 18$ and $m \mid 12$, then $m$ must also divide which of these?
* (A) 5
* (B) 6
* (C) 7
* (D) 8

**Q4.** If $4 \mid (n + 5)$ and $4 \mid 5$, what must be true about $n$?
* (A) $n$ must be 4
* (B) $n$ must be divisible by 4
* (C) $n$ must be an odd number
* (D) $n$ must be 0

**Q5.** Suppose $m \mid a$ and $m \mid b$. If the difference $a - b = 7$, what is the largest possible value for $m$ (where $m > 1$)?
* (A) 7
* (B) 2
* (C) 3
* (D) 14

---

### 📝 Part 3: The Combo Rule (Linear Combination)

**Q6.** If $k$ divides $a$ and $k$ divides $b$, then $k$ **must** divide:
* (A) $a \times b + 1$
* (B) $2a + 3b$
* (C) $a + 1$
* (D) $b - 1$

**Q7.** Given $11 \mid x$ and $11 \mid y$, which of these is definitely a member of the **"Divisible by 11" Clan**?
* (A) $x + y + 1$
* (B) $2x - y$
* (C) $x / y$
* (D) $11x + 5$

---

### 📝 Part 4: The "N-Elimination" Logic

**Q8.** If $m$ divides $(n + 1)$ and $m$ also divides $(n + 3)$, what is the largest possible value for $m$?
* (A) 1
* (B) 2
* (C) 3
* (D) 4

**Q10.** If $m > 1$ and $m$ divides both $(2n + 4)$ and $(2n + 2)$, what is the value of $m$?
* (A) 2
* (B) 3
* (C) 4
* (D) 5

**Q10.** If $m$ is a positive integer and $m \mid (10n + 7)$ and $m \mid (10n + 6)$, then $m$ must be:
* (A) 10
* (B) 5
* (C) 1
* (D) $n$

---

# 🔑 Answer Key & Logic

| Question | Answer | Math Logic |
| :--- | :--- | :--- |
| **Q1** | **(C)** | 3 does not divide 10 ($10 \div 3 = 3$ r $1$). |
| **Q2** | **(B)** | 5 divides 10, and 10 divides 20. |
| **Q3** | **(B)** | $18 - 12 = 6$. By Rule 2, $m$ divides 6. |
| **Q4** | **(B)** | $(n+5) - (5) = n$. By Rule 2, 4 must divide $n$. |
| **Q5** | **(A)** | $m$ must divide the difference (7). Only 1 and 7 divide 7. |
| **Q6** | **(B)** | Rule 3: Any combination $(qa + rb)$ is divisible by $k$. |
| **Q7** | **(B)** | $2x - 1y$ is a linear combination ($q=2, r=-1$). |
| **Q8** | **(B)** | $(n+3) - (n+1) = 2$. $m$ must divide 2. |
| **Q9** | **(A)** | $(2n+4) - (2n+2) = 2$. The only integer $>1$ dividing 2 is 2. |
| **Q10** | **(C)** | $(10n+7) - (10n+6) = 1$. Only 1 can divide 1. |
