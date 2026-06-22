# 🎓 The Secrets of the GCD (Greatest Common Divisor)
**Topic:** Common Divisors, Coprimality, and the "Shrink Rule"
**Date:** February,24 2026

---

### 1. What is a Common Divisor? 
If we have a group of numbers $a_1, a_2, \dots, a_n$, and a number $d$ divides **every single one** of them, then $d$ is a **Common Divisor**.
* **The Leader (GCD):** The largest of these common divisors is called the **Greatest Common Divisor**, written as $(a_1, a_2, \dots, a_n) = d$.

> **Example:** Consider the numbers **12** and **18**.
> * **GCD (The Leader):** $(12, 18) = 6$

---

### 2. The Absolute Value Theorem
**Theorem 1:** $GCD(a, b) = GCD(|a|, |b|)$
* **Logic:** The Greatest Common Divisor is independent of the sign of the integers. 
* **Application:** In competitive math and programming, always convert numbers to their absolute values first to simplify the calculation.

> **Example:** > Find the GCD of **-10** and **15**.
> * $|-10| = 10$ and $|15| = 15$.
> * $(10, 15) = 5$.
> * Result: $(-10, 15) = 5$. The "minus" sign doesn't change the common factors!

---

### 3. The Zero Element Theorem (Boundary Case)
**Theorem 2:** If $b \neq 0$, then $GCD(0, b) = |b|$
* **Logic:** Since every integer divides $0$, the largest integer that divides both $0$ and $b$ is the largest divisor of $b$ itself, which is $|b|$.
* **Application:** This acts as the **Termination Condition** in your code. When the remainder reaches $0$, the other number is your answer.

> **Example:** Find $(0, 7)$.
> * Every number divides 0 (0 ÷ 1, 0 ÷ 2... all work).
> * The divisors of 7 are {1, 7}.
> * The largest common factor is **7**.
> * Result: $(0, 7) = 7$.

---

### 4. The "Shrinking Rule" (Euclidean Algorithm)
**Theorem 3:** If $a = bq + c$, then $GCD(a, b) = GCD(b, c)$
### 🔍 Why? (The Proof Logic)

* **Linear Combination:** If $d|a$ and $d|b$, then $d$ must divide any linear combination of them, such as $c = a - bq$.
* **Shared Identity:** Since $d$ divides $a, b,$ and $c$, it follows that $a, b,$ and $c$ all **share the same set** of common divisors.
* **Identical Sets:** Therefore, the set of common divisors for the pair $(a, b)$ and the pair $(b, c)$ is **identical**.
* **GCD Equality:** Since they share the exact same divisors, they must share the same Greatest Common Divisor (GCD).

**Conclusion:**
$$(a, b) = (b, c)$$

#### **The Special Properties:**
* **Property 1 (Nesting):** $(a, b, c) = ((a, b), c)$. You can find the GCD of a big group by doing it in pairs.
* **Property 2 (Add/Sub):** $(a, b) = (a - b, b)$. Subtracting the smaller number from the larger one doesn't change the GCD.
* **Property 3 (Multi-Jump):** $(a, b) = (a + kb, b)$ for any integer $k$.

> **Example of Property 2 (Subtraction): Find $(20, 8)$.**
> * Step 1: $(20 - 8, 8) = (12, 8)$.
> * Step 2: $(12 - 8, 8) = (4, 8)$.
> * Step 3: $(8 - 4, 4) = (4, 4) = 4$.
> * **Result:** $(20, 8) = 4$.

> **Example of Property 3 (Modulo):Find $(20, 8)$**
> * Step 1: $(20, 8) \to (8, 20 \pmod 8) = (8, 4)$.
> * Step 2: $(8, 4) \to (4, 8 \pmod 4) = (4, 0)$.
> * **Result:** The last non-zero remainder is **4**.

---
### 🐍 Python Tip
Use math.gcd (a,b) to calculate GCD in PyCharm:
```python
# Subtraction-based Euclidean Algorithm
# Find gcd(a, b) using repeated subtraction

# Input two numbers
a = 20
b = 8

# Loop until both numbers are equal
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

# Print the result
print("GCD:", a)
 ````
```python
# Euclidean Algorithm using Modulo (%)
a = 20
b = 8

# Loop until b = 0 
while b != 0:
    # The Logic: GCD(a, b) is the same as GCD(b, a % b)
    a, b = b, a % b
    
print(f"GCD is: {a}")
 ````
---

## ✍️ Practice Challenge

**Q1. The Group Leader**
Find the GCD for the following groups:
1. $(10, 15, 20) = \dots$
2. $(7, 14, 21) = \dots$

**Q2. The Coprime Detective**
Look at the group $\{6, 10, 15\}$.
1. Is the GCD of the group $(6, 10, 15) = 1$? (Yes/No)
2. Is the pair $(10, 15)$ coprime? (Yes/No)

**Q3. The Shrink Challenge**
We want to find the GCD of $(50, 20)$.
1. First, write the division: $50 = 20 \times 2 + (\dots)$
2. Use the rule $(a, b) = (b, c)$. What is the new smaller pair? $(\dots, \dots)$
3. What is the final GCD?

**Q4. Property of Zero**
What is the GCD of $(0, -13)$?
*(Hint: Look at the Absolute Value rule in Section 1).*

---

# 🔑 Answer Key

| Question | Answer |
| :--- | :--- |
| **Q1.1** (10, 15, 20) | **5** |
| **Q1.2** (7, 14, 21) | **7** |
| **Q2.1** (6, 10, 15) GCD = 1? | **Yes** |
| **Q2.2** (10, 15) Coprime? | **No** |
| **Q3.1** 50 = 20 * 2 + [?] | **10** |
| **Q3.2** New Pair (b, r) | **(20, 10)** |
| **Q3.3** Final GCD | **10** |
| **Q4** gcd(0, -13) | **13** |