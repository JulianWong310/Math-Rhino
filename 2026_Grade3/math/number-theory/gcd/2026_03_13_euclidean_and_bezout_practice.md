# 🏆  Euclidean Properties & Bézout's Identity
---

### 📝 Questions

**Q1. What is the value of $GCD(0, -2026)$?**
* (A) 0  
* (B) 1  
* (C) -2026  
* (D) 2026  
* (E) Undefined

**Q2. Which of the following pairs is guaranteed to be coprime ($GCD=1$) according to the Consecutive Integer Rule?**
* (A) $(2024, 2026)$  
* (B) $(1234567, 1234568)$  
* (C) $(15, 25)$  
* (D) $(10, 20)$  
* (E) $(100, 102)$

**Q3. If $GCD(a, b) = 12$, what is the value of $GCD(5a, 5b)$ using the Scaling Up property?**
* (A) 12  
* (B) 17  
* (C) 60  
* (D) 120  
* (E) 5

**Q4. According to the Scaling Down property, if $GCD(143, 77) = 11$, what is $GCD(\frac{143}{11}, \frac{77}{11})$?**
* (A) 1  
* (B) 7  
* (C) 11  
* (D) 13  
* (E) 121

**Q5. In the Euclidean Algorithm for $GCD(252, 105)$, the first step is $252 = 105 \times 2 + 42$. According to Theorem 4, this means $GCD(252, 105)$ is equal to:**
* (A) $GCD(252, 42)$  
* (B) $GCD(105, 42)$  
* (C) $GCD(252, 2)$  
* (D) $GCD(105, 2)$  
* (E) $GCD(42, 2)$

**Q6. Using the Associative Property (Theorem 5C), find $GCD(12, 18, 30)$.**
* (A) 2  
* (B) 3  
* (C) 6  
* (D) 12  
* (E) 1

**Q7. If the final non-zero remainder in a Euclidean Algorithm chain is $r_n = 21$, what is the GCD of the original two numbers $(a, b)$?**
* (A) 1  
* (B) $r_{n-1}$  
* (C) 21  
* (D) 0  
* (E) $a+b$

**Q8. What is $GCD(-15, -25)$?**
* (A) -5  
* (B) 5  
* (C) 15  
* (D) 25  
* (E) -1

**Q9. If $GCD(x, y) = d$, which of the following must be true about $GCD(\frac{x}{d}, \frac{y}{d})$?**
* (A) It is equal to $d$.  
* (B) It is equal to $0$.  
* (C) It is equal to $1$.  
* (D) It is equal to $x/y$.  
* (E) It cannot be determined.

**Q10. Apply the Euclidean chain to $GCD(105, 42)$. What is the last non-zero remainder?**
* (A) 42  
* (B) 21  
* (C) 1  
* (D) 7  
* (E) 3

**Q11. According to Bezout’s Identity, if $GCD(24, 9) = 3$, what is the smallest positive integer that can be expressed in the form $24s + 9t$ for integers $s$ and $t$?**
* (A) 1  
* (B) 2  
* (C) 3  
* (D) 6  
* (E) 9

**Q12. If $15s + 20t = k$ has integer solutions for $s$ and $t$, which of the following is a possible value for $k$?**
* (A) 2  
* (B) 8  
* (C) 10  
* (D) 12  
* (E) 14

**Q13. If $GCD(a, b) = d$, and we know $as + bt = 7$ for some integers $s$ and $t$, what are the possible values for $d$?**
* (A) Only 7  
* (B) Only 1  
* (C) 1 or 7  
* (D) Any multiple of 7  
* (E) Any divisor of $a$

**Q14. Which property allows us to state that $GCD(a, b) = GCD(a, b - ka)$?**
* (A) Scaling Property  
* (B) Linearity Property (Linear Combination)  
* (C) Identity Property  
* (D) Associative Property  
* (E) Commutative Property

**Q15. If $n$ is an integer, what is the $GCD(n, n+2)$ if $n$ is an even number?**
* (A) 1  
* (B) 2  
* (C) $n$  
* (D) $n+2$  
* (E) 4

---

### 🗝️ Answer Key & Logic Hook

* **Q1: (D)** — **Zero Case:** $GCD(0, b) = |b|$. GCD is always a positive magnitude.
* **Q2: (B)** — **Consecutive Rule:** $\gcd(n, n+1)$ is always 1.
* **Q3: (B)** — **Scaling Up:** $\gcd(ka, kb) = k \cdot \gcd(a, b) = 5 \times 12 = 60$.
* **Q4: (A)** — **Scaling Down:** $\gcd(a/d, b/d) = 1$. Dividing by the GCD leaves no common factors.
* **Q5: (A)** — **Theorem 4:** $\gcd(a, b) = \gcd(b, r)$. Replace the dividend with the remainder.
* **Q8: (B)** — **Absolute Value:** Signs don't matter; $\gcd(a, b) = \gcd(|a|, |b|)$.
* **Q11: (B)** — **Bezout's Lemma:** Min positive $as + bt$ is exactly $\gcd(a, b)$.
* **Q12: (B)** — **Multiple Rule:** $k$ must be a multiple of $\gcd(15, 20)=5$.
* **Q13: (B)** — **Divisibility:** The GCD must be a divisor of the combination result (7).
* **Q15: (B)** — **Even Property:** Difference is 2 and both share 2, so the GCD is 2.$n+2$ share a factor of 2. Since their difference is only 2, the GCD cannot be larger than 2.