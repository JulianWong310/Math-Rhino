# 🏆 The Congruence Detective (Modular Arithmetic)

> **Topic:** Congruence Modulo $b$ & The Gap Rule
> **Goal:** Practice identifying "Clock Matches" using properties.

---

### 📝 Practice Questions

**1. If $a \equiv 3 \pmod 7$, which of the following could be the value of $a$?**
* (A) 10
* (B) 14
* (C) 15
* (D) 17
* (E) 20

**2. According to the "Gap Rule" (Difference Rule), $a \equiv r \pmod b$ is true only if $b$ divides $(a-r)$. Using this, which statement is FALSE?**
* (A) $17 \equiv 2 \pmod 5$
* (B) $24 \equiv 4 \pmod {10}$
* (C) $11 \equiv 1 \pmod 2$
* (D) $30 \equiv 5 \pmod 6$
* (E) $100 \equiv 10 \pmod {30}$

**3. If today is Monday (Day 1) and there are 7 days in a week, what day will it be in 100 days?**
*(Hint: Find $100 \equiv r \pmod 7$)*
* (A) Monday
* (B) Tuesday
* (C) Wednesday
* (D) Thursday
* (E) Friday



**4. The "Mirror Rule" (Symmetry) says if $a \equiv r \pmod b$, then $r \equiv a \pmod b$. If $x \equiv 5 \pmod 9$, which of these must also be true?**
* (A) $9 \equiv 5 \pmod x$
* (B) $5 \equiv x \pmod 9$
* (C) $x+9 = 5$
* (D) $x$ is a multiple of 5
* (E) $x$ is 14

**5. What is the remainder $r$ when $(20 + 31 + 42)$ is divided by 10?**
*(Hint: You can find the $r$ of each part first: $20 \equiv 0$, $31 \equiv 1$, $42 \equiv 2 \pmod{10}$)*
* (A) 1
* (B) 2
* (C) 3
* (D) 4
* (E) 0

**6. If $n \equiv 2 \pmod 3$, what is the remainder $r$ when $n + 10$ is divided by 3?**
* (A) 0
* (B) 1
* (C) 2
* (D) 3
* (E) 12

**7. Which of the following numbers is congruent to $1 \pmod 4$ AND congruent to $1 \pmod 5$?**
*(In other words, $x \equiv 1 \pmod 4$ and $x \equiv 1 \pmod 5$)*
* (A) 6
* (B) 11
* (C) 16
* (D) 21
* (E) 26

**8. Using the "Chain Rule" (Transitivity): If $A \equiv B \pmod b$ and $B \equiv r \pmod b$, then $A \equiv r \pmod b$. If $x \equiv 45 \pmod {10}$ and $45 \equiv 5 \pmod {10}$, what is $x \equiv ? \pmod{10}$?**
* (A) 0
* (B) 5
* (C) 10
* (D) 40
* (E) 50

**9. What is the smallest positive integer $x > 1$ such that $x \equiv 1 \pmod 2, x \equiv 1 \pmod 3,$ and $x \equiv 1 \pmod 5$?**
* (A) 11
* (B) 16
* (C) 21
* (D) 31
* (E) 61



**10. If $48 \equiv 12 \pmod b$, and $b$ is a prime brick greater than 5, what is the value of $b$?**
*(Hint: $b$ must divide the gap $48 - 12 = 36$. Find the prime bricks of 36!)*
* (A) 2
* (B) 3
* (C) 7
* (D) 11
* (E) No such prime exists

---

## 🔑 Answer Key

1. **A** ($10 - 3 = 7$, which is $7 \times 1$)
2. **D** ($30 - 5 = 25$, but 6 does not divide 25)
3. **C** ($100 = 7 \times 14 + 2$. Monday + 2 days = Wednesday)
4. **B** (Direct application of Symmetry)
5. **C** ($0 + 1 + 2 = 3$)
6. **A** ($2 + 10 = 12$, and $12 \equiv 0 \pmod 3$)
7. **D** ($21-1=20$, which is a multiple of both 4 and 5)
8. **B** (Direct application of Transitivity)
9. **D** (The number must be $LCM(2,3,5) + 1 = 30 + 1$)
10. **E** (36's prime bricks are 2 and 3. Neither is $> 5$)