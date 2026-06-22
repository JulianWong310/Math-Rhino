# 🏆 Number Theory Practice

---

## 📝 Part 1: Multiple Choice Questions

**Q1. What is the greatest common divisor of $120$ and $45$?**

(A) 5  
(B) 10  
(C) 15  
(D) 25  
(E) 45  

---

**Q2. If $\gcd(a, b) = 1$, which of the following must be true according to Bézout's Identity?**

(A) $a + b = 1$  
(B) There exist integers $s$ and $t$ such that $as + bt = 1$  
(C) $a$ and $b$ are both prime numbers  
(D) $ab = 1$  
(E) $a$ is a multiple of $b$  

---

**Q3. Julian finds that $3 \times (2) + 5 \times (-1) = 1$. What does this tell him about the numbers $3$ and $5$?**

(A) They are both even  
(B) Their sum is 1  
(C) They are coprime (their GCD is 1)  
(D) 5 divided by 3 has a remainder of 1  
(E) They have no multiples  

---

**Q4. Given that $\gcd(101, 3) = 1$, what is the value of $\gcd(101 \times 12, 3)$ based on Theorem 2?**

(A) 1  
(B) 3  
(C) 101  
(D) 303  
(E) 12  

---

**Q5. If $n$ is an integer such that $\gcd(n, 7) = 1$ and $7$ divides $3n$, what does Euclid's Lemma (Corollary 1) say?**

(A) $7$ must divide $3$  
(B) $3$ must divide $7$  
(C) $7$ must divide $n$  
(D) $3n$ must be 1  
(E) The lemma doesn't apply  

---

**Q6. Using the linear combination $2s + 5t = 1$, if we multiply both sides by $4$, we get $8s + 20t = 4$. This proves that:**

(A) $\gcd(8, 20) = 4$  
(B) $4$ is a common divisor of $8$ and $20$  
(C) $4$ can be written as a combination of $8$ and $20$  
(D) $s$ must be 4  
(E) $\gcd(2, 5) = 4$  

---

**Q7. How many pairs of integers $(s, t)$ can satisfy the equation $2s + 4t = 1$?**

(A) 0 (Because $\gcd(2, 4) = 2$, and 2 does not divide 1)  
(B) 1  
(C) 2  
(D) 4  
(E) Infinitely many  

---

**Q8. If $\gcd(a, c) = 1$ and $\gcd(b, c) = 1$, what is $\gcd(ab, c)$ according to Corollary 3?**

(A) $a+b$  
(B) $c$  
(C) 1  
(D) $ab$  
(E) It depends on $a$ and $b$  

---

**Q9. Which of the following values for $k$ would make the equation $14s + 21t = k$ possible for some integers $s$ and $t$?**

(A) 1  
(B) 3  
(C) 5  
(D) 7 (Because $\gcd(14, 21) = 7$)  
(E) 10  

---

**Q10. If $\gcd(a, c) = 1$, then the set of common divisors of $(ab, c)$ is identical to the set of common divisors of:**

(A) $(a, b)$  
(B) $(a, c)$  
(C) $(b, c)$  
(D) $(ab, b)$  
(E) $(s, t)$  

---

## 🔑 Part 2: Answer Key & Logic

| Question | Answer | Logic Summary |
| :--- |:-------| :--- |
| **Q1** | **C**  | $120 = 15 \times 8$ and $45 = 15 \times 3$. $\gcd = 15$. |
| **Q2** | **B**  | Definition of Bézout's Identity: $as+bt = \gcd(a,b)$. |
| **Q3** | **C**  | If a linear combination equals 1, then $\gcd(3, 5) = 1$. |
| **Q4** | **B**  | Since $\gcd(101, 3)=1$, $\gcd(101 \cdot 12, 3) = \gcd(12, 3) = 3$. |
| **Q5** | **A**  | $c \mid ab$ and $(a,c)=1 \implies c \mid b$. Here $7 \mid 3n$ and $(7,n)=1 \implies 7 \mid 3$. |
| **Q6** | **C**  | Multiplication shows $4$ is a linear combination of $8$ and $20$. |
| **Q7** | **A**  | $2s+4t=1$ has no integer solutions because $\gcd(2,4)=2$, and $2 \nmid 1$. |
| **Q8** | **C**  | Product of numbers coprime to $c$ remains coprime to $c$. |
| **Q9** | **D**  | $k$ must be a multiple of $\gcd(14, 21) = 7$. |
| **Q10** | **C**  | Theorem 2: If $(a,c)=1$, then $(ab, c) = (b, c)$. |