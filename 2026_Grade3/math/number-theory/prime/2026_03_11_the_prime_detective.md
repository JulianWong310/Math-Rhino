# 📔 Number Theory Lab: The Prime Detective 

> **Goal:** Understand Theorem 1 and Theorem 2 about Primes.
> **Primes:** Numbers > 1 that can only be divided by 1 and themselves. 

---

### 🕵️‍♂️ Theorem 1: The Smallest Prime Factor Theorem
**The Math:** If $a > 1$ is a composite number, its smallest divisor $q$ (other than 1) must be a **Prime**, and $q \leq \sqrt{a}$.

#### 📝 Mathematical Proof:
1. Since $a$ is a composite number, we can write $a = q \cdot N$, where $N > 1$.
2. Because $q$ is the smallest divisor (excluding 1), we know that $N \leq q$.
3. Multiply both sides by $q$: 
   $$q^2 \leq q \cdot N = a$$
4. Taking the square root of both sides, we get:
   $$q \leq \sqrt{a}$$


>**Example:** Is 97 a Prime?
>* $\sqrt{97}$ is about 9.8.
>* You only need to check primes: 2, 3, 5, 7.
>* None of them divide 97. **Conclusion:** 97 is a Prime!

---
### 🤝 Theorem 2: The Coprime Property of Primes

**Statement:** Let $p$ be a Prime and $a \in \mathbb{Z}^+$. Then either $p | a$ OR $(p, a) = 1$.

#### 📝 Mathematical Proof (From Julian's Notes):

1. Let $d$ be the Greatest Common Divisor of $p$ and $a$, so $d = (p, a)$.
2. Since $d$ is a divisor of $p$ ($d | p$), and $p$ is a prime, the only possible values for $d$ are **1** or **$p$**.
3. **Case 1**: If $d = 1$, then $(p, a) = 1$. (They are coprime).
4. **Case 2**: If $d = p$, then since $d$ is also a divisor of $a$ ($d | a$), we conclude that $p | a$.

---

**The Logic:**
Primes are "stubborn." Let's say Prime $p=3$:
* If $a=6$: $3$ goes into $6$ perfectly. ($p | a$)
* If $a=10$: $3$ and $10$ have **nothing** in common except the number 1. ($\gcd(3, 10) = 1$)
* There is no "middle ground." A Prime never shares "half" 

**Corollary (Important for Coding!):** If a Prime $p$ divides a product $a \cdot b$, then $p$ **must** divide $a$ or $p$ **must** divide $b$.
* *Python Example:* If `(x * y) % 7 == 0`, then either `x % 7 == 0` or `y % 7 == 0`.

---

### 📝 Practice Set

#### Task 1: Applying Theorem 1 (The Square Root Shortcut)
**Question:** Is **127** a Prime? Follow these steps:
1. Calculate $\sqrt{127} \approx 11.2$.
2. List all primes $q \leq 11$: `{2, 3, 5, 7, 11}`.
3. Test divisibility: 
   - 127 is not even (No 2)
   - $1+2+7=10$ (No 3)
   - Ends in 7 (No 5)
   - $127 = 7 \times 18 + 1$ (No 7)
   - $127 = 11 \times 11 + 6$ (No 11)
4. **Conclusion:** __________

#### Task 2: Applying Theorem 2 (The Either/Or Rule)
**Question:** Given $p = 7$ and $a = 20$.
1. Does $7 | 20$? (Yes/No) __________
2. What is the GCD $(7, 20)$? __________
3. Does this satisfy Theorem 2 (Either $p|a$ or $(p,a)=1$)? __________

#### Task 3: The Multi-Part Product (Corollary Challenge)
**Question:** If $11 | (33 \cdot x \cdot 15)$ and we know $11 \nmid 15$.
Based on the Corollary, which of the following is true?
* (A) 11 must divide $x$.
* (B) 11 already divides 33, so $x$ can be any integer.
* (C) 11 must divide both 33 and $x$.

---

## 🔑 Answer Key & Logic 

| Task | Answer | Logic / Explanation                                                                                                                                                  |
| :--- | :--- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1.3** | **None of them** | None of the primes up to $\sqrt{127}$ divide 127.                                                                                                                    |
| **1.4** | **127 is Prime** | Per **Theorem 1**, if no prime $\leq \sqrt{a}$ divides $a$, then $a$ is prime.                                                                                       |
| **2.1** | **No** | 20 is not a multiple of 7.                                                                                                                                           |
| **2.2** | **1** | 7 and 20 share no common factors other than 1.                                                                                                                       |
| **2.3** | **Yes** | Since $7 \nmid 20$, then $(7, 20)$ must be 1. It fits the "Either/Or" rule.                                                                                          |
| **3** | **(B)** | The Corollary says $p$ must divide **at least one** part. Since $11  33$ is already true ($33 = 11 \times 3$), the condition is satisfied regardless of what $x$ is! |

---

