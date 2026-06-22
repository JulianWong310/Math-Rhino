# 🏆 GCD & Coprimality: Master Practice 

---

### 🟢 Level 1: Quick Fire

**1. Simplify the expression: $\gcd(2n+1, n)$ for any positive integer $n$.**
* (A) $n$
* (B) 2
* (C) 1
* (D) 3

**2. If $\gcd(a, b) = 12$, what is the value of $\gcd(5a, 5b)$?**
* (A) 12
* (B) 60
* (C) 17
* (D) 5

**3. Which of the following pairs is ALWAYS coprime for any positive integer $n$?**
* (A) $n, n+2$
* (B) $n, 2n$
* (C) $n, n+1$
* (D) $2n, 2n+2$

**4. Simplify $\gcd(10k+7, 2k+1)$.**
* (A) 2
* (B) $k$
* (C) 5
* (D) 1

**5. Given $\gcd(x, y) = 1$, find $\gcd(x+y, x-y)$ if both $x$ and $y$ are odd.**
* (A) 1
* (B) 2
* (C) 4
* (D) $x$

---

### 🟡 Level 2: Intermediate Tactical

**6. If $\gcd(a, c) = 1$, simplify $\gcd(ac, b)$.**
* (A) $\gcd(a, b) \cdot \gcd(c, b)$
* (B) $\gcd(a, c)$
* (C) $b$
* (D) 1

**7. Evaluate $\gcd(120, 50, 20)$ using the Associative Property.**
* (A) 5
* (B) 20
* (C) 10
* (D) 1

**8. If $\gcd(a, b) = 1$, which of the following must be true?**
* (A) $\gcd(a+b, a) = 1$
* (B) $\gcd(a, 2b) = 1$
* (C) $a$ must be prime
* (D) $\gcd(a, b^2) = b$

**9. Simplify $\gcd(3n+2, 2n+1)$.**
* (A) $n+1$
* (B) 2
* (C) 1
* (D) 3

**10. If $\gcd(a, b) = d$, then $\gcd(a/d, b/d)$ is:**
* (A) $d$
* (B) $a/b$
* (C) 1
* (D) 0

---

### 🔴 Level 3: Master Challenges

**11. Find the value of $\gcd(n!+1, n)$ for $n > 1$.**
* (A) $n$
* (B) 1
* (C) $n!$
* (D) $n-1$

**12. Determine $\gcd(k, k+1, k+2)$ for any positive integer $k$.**
* (A) 1
* (B) 2
* (C) $k$
* (D) 3

**13. For a prime $p > 3$, calculate $\gcd(p, 6)$.**
* (A) 2
* (B) 3
* (C) 6
* (D) 1

**14. If $5x + 7y = 1$ has integer solutions, what is $\gcd(5, 7)$?**
* (A) 5
* (B) 1
* (C) 35
* (D) 0

**15. Simplify the expression: $\gcd(n^2+1, n+1)$.**
* (A) $\gcd(2, n+1)$
* (B) 1
* (C) $n+1$
* (D) 2

---

# 🔑 Answer Key & Master's Hints

| Q# | Ans | Master's Hint (The Logic) |
| :--- | :--- | :--- |
| 1 | **C** | Subtract $2 \times n$ from the first term. |
| 2 | **B** | Factoring out the $k$: $\gcd(ka, kb) = k \cdot \gcd(a, b)$. |
| 3 | **C** | Their difference is 1, and only 1 can divide 1. |
| 4 | **D** | Subtract $5 \times (2k+1)$ from $10k+7$. What's left? |
| 5 | **B** | Both are even, but $\gcd(x,y)=1$ limits the factors. |
| 6 | **A** | Stranger Rule: Coprime $a, c$ don't "interfere" with each other. |
| 7 | **C** | Solve step-by-step: $\gcd(120, 50)$ first. |
| 8 | **A** | Basic Shift: $\gcd(a+b, a) = \gcd(b, a)$. |
| 9 | **C** | Two shifts: first subtract $2n+1$, then look at what's left. |
| 10 | **C** | Scaling Down: Dividing by the GCD leaves no common factors. |
| 11 | **B** | $n!$ is a multiple of $n$. What is the remainder of $n!+1$? |
| 12 | **A** | Since $\gcd(k, k+1)=1$, the third number doesn't matter. |
| 13 | **D** | Prime $p > 3$ is not even and not a multiple of 3. |
| 14 | **B** | Bézout's Identity: If $ax+by=1$, they must be coprime. |
| 15 | **A** | Factor $n^2-1 = (n+1)(n-1)$ and use the Shift Rule. |