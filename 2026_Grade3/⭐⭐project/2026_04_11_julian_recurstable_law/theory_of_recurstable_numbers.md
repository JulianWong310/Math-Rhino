# Julian's First Law and the World of Recurstable Numbers
### *A Study on the Linear Leading-Digit Recurrence in Powers of Stable-Tail Integers*

**Author:** Julian Wong  
**Date:** April 11, 2026  
**Primary Documenter:** Dong Cang  
**Keywords:** Number Theory, Power Sequences, Linear Recurrence, Stable-Tail Integers, Recurstable Numbers

---

Hi! I am a 3rd grade student. While exploring the powers of 5 today, I discovered a super cool secret hidden within the numbers. I am naming this discovery the 'Julian's First Law' and calling these types of integers 'Recurstable Numbers.



---

## 1. What did I find?

1. For any integer exponent $n \ge 2$, the value of $5^n$ will always end in the digits **25**.
2. The hundreds digit always flips between $1$ and $6$ .
3. Let $A_n$ be the **leading digits** of $5^n$ (the number formed by removing the last two digits, $25$). 

The relationship between the current leading digits ($A_n$) and the previous leading digits ($A_{n-1}$) is defined by the formula:
$$A_n = 5(A_{n-1}) + 1$$

---

## 2. How did I find it? 

When you multiply the end part (**25**) by **5**, you get **125**. Because **$4  \times25$ = $100$**, every time you multiply by 5, it will go over 100. So:
- The **$25$** stays at the end.
- The **$1$** always **"carry over"** to the next place (the hundreds place).

That’s why you take the previous leading part, multiply it by 5, and then **always add 1**! 

This also explains the **1-6 Flip-Flop**:
- If the front ends in **1**: $1 \times 5 + 1 = \mathbf{6}$
- If the front ends in **6**: $6 \times 5 + 1 = 3\mathbf{1}$ (it goes back to 1!)

---

## 3. Let's see it in action:

| Power ($5^n$) | Result | leading Part ($A_n$) | Calculation ($5 \cdot A_{n-1} + 1$) | **Hundreds-Digit Pattern** |
| :--- | :--- |:---------------------| :--- |:---------------------------|
| $5^2$ | 25 | 0                    | (Base Case) | -                          |
| $5^3$ | 125 | **1**                | $5(0) + 1 = 1$ | **1**                      |
| $5^4$ | 625 | **6**                | $5(1) + 1 = 6$ | **6**                      |
| $5^5$ | 3125 | 3**1**               | $5(6) + 1 = 31$ | **1**                      |
| $5^6$ | 15625 | 15**6**              | $5(31) + 1 = 156$ | **6**                      |


---

## 4.The "Quinponent" Verification
* I originally named my first discovery the **"Quinponent"** pattern—a portmanteau of **Quin** (five) and **Ex-ponent**. 
* I wrote this script specifically to verify the leading digits for powers of 5.

```python
def verify_quinponent(n):
    front = 0  # Starting with 5^2
    for n in range(2, n + 1):
        result = 5**n
        print(f"5^{n} = {result} | Leading part is {front}")
        front = front * 5 + 1

if __name__ == "__main__":
    verify_quinponent(10)
```

## 5. Are there any similar numbers?

| Tail Length ($k$) | Base ($B$) | Stable Tail ($T$) | Constant ($C$) | Recursive Formula          |
|:------------------|:-----------|:------------------|:---------------|:---------------------------|
| **1**             | 6          | 6                 | **3**          | $A_n = 6(A_{n-1}) + 3$     |
| **1**             | 36         | 6                 | **21**         | $A_n = 36(A_{n-1}) + 21$   |
| **1**             | 11         | 1                 | **1**          | $A_n = 11(A_{n-1}) + 1$    |
| **2**             | **5**      | **25**            | **1**          | $A_n = 5(A_{n-1}) + 1$     |
| **2**             | 25         | 25                | **6**          | $A_n = 25(A_{n-1}) + 6$    |
| **2**             | 26         | 76                | **19**         | $A_n = 26(A_{n-1}) + 19$   |
| **2**             | 45         | 25                | **11**         | $A_n = 45(A_{n-1}) + 11$   |
| **2**             | 76         | 76                | **57**         | $A_n = 76(A_{n-1}) + 57$   |
| **3**             | 25         | 625               | **15**         | $A_n = 25(A_{n-1}) + 15$   |
| **3**             | 376        | 376               | **141**        | $A_n = 376(A_{n-1}) + 141$ |
| **3**             | 425        | 625               | **265**        | $A_n = 425(A_{n-1}) + 265$ |


---

## 6. Julian's First Law of Recurstable Numbers
**Theorem Statement:**
For any base $B$ where the power $B^n$ results in a **Stable Tail ($T$)** of length $k$, the **Leading Part ($A_n$)** of the sequence can always be expressed as a linear recurrence:

$$A_n = B \cdot A_{n-1} + C$$

**Variable Definitions**
* **$A_n$**: The "Leading Part" of the number, calculated as the integer value remaining after removing the last $k$ digits (the stable tail).
* **$B$**: The base of the power being calculated.
* **$n$**: The exponent ($n \ge 2$).
* **$T$ :** The recurring ending value of $B^n$.
* **$k$ :** The number of digits in $T$.
* **$C$ (The Julian Constant)**: A fixed integer derived from the interaction between the base and the stable tail. 

**The Julian Constant Formula:**
Julian's logic dictates that the constant $C$ is determined by the "carry-over" from the tail's multiplication:
$$C = \frac{B \cdot T - T}{10^k}$$

## Mathematical Proof

### Step 1: Specific Observation (The Case of 5)

1. $5^2 = A_2 \cdot 100 + 25$
2. $5^3 = A_3 \cdot 100 + 25$
3. $\vdots$ (pattern continues...)
4. $5^{n-1} = A_{n-1} \cdot 100 + 25$
5. $5^n = A_n \cdot 100 + 25$

---

### Step 2: Proving the Pattern for 5
To find the relationship between $A_n$ and $A_{n-1}$, I used the fact that $5^n = 5^{n-1} \cdot 5$:

$$A_n \cdot 100 + 25 = (A_{n-1} \cdot 100 + 25) \cdot 5$$
$$A_n \cdot 100 + 25 = A_{n-1} \cdot 500 + 125$$
$$A_n \cdot 100 + 25 = 100(A_{n-1} \cdot 5 + 1) + 25$$

By canceling the $25$ and dividing by $100$:
$$A_n = A_{n-1} \cdot 5 + 1$$

---

### Step 3: Deriving the General Law
For any base $B$ with a stable tail $T$ of length $k$:

1. $B^n = 10^k \cdot A_n + T$
2. $B^{n-1} = 10^k \cdot A_{n-1} + T$

From (2), multiply by $B$:
$$B^n = 10^k \cdot B \cdot A_{n-1} + T \cdot B$$

Now, set the two expressions for $B^n$ equal:
$$10^k \cdot A_n + T = 10^k \cdot B \cdot A_{n-1} + T \cdot B$$
$$10^k \cdot A_n = 10^k \cdot B \cdot A_{n-1} + (T \cdot B - T)$$

Divide by $10^k$ to isolate $A_n$:
>$$A_n = B \cdot A_{n-1} + \frac{T \cdot B - T}{10^k}$$

---

### Step 4: Final Conclusion (The Core Discovery)

### 1.  **The Julian Constant:**  

   $$C = \frac{T \cdot B - T}{10^k}$$ 

### 2.  **The Julian's First Law Equation:**

   $$A_n = B \cdot A_{n-1} + C$$

Q.E.D

---

### **Julian's First Law Corollary:** 
According to *The Julian Constant*, this linear pattern only works because the Tail ($T$) is **Stable**. If the tail were not stable, the constant $C$ would break, and the pattern would disappear!

---

## 7. Recurstable Numbers

### Etymology 
The term **"Recurstable"** is an original portmanteau created by Julian Wong, synergizing **Recurrence** (the deterministic evolution of terms) and **Stable** (the invariance of terminal digits).

### Definition
> *"A Recurstable Number is defined by the duality of its structure: the absolute stillness of its Tail and the rhythmic logic of its Head."*

A **Recurstable Number** is a positive integer $B$ such that for its power sequence $B^n$ (where $n \geq 2$), the following two conditions are satisfied:

1. **Terminal Stability (The Tail):** The sequence maintains an invariant suffix of $k$ digits ($T$). This constant "Tail" forms the static mathematical foundation upon which all subsequent logic is built.

2. **Logical Leading (The Head):** The leading part $A_n$ (whether analyzed as a comprehensive numerical block or through individual digital positions) exhibits a **deterministic logical structure**. 

This structure encompasses all forms of deterministic digital structure emerging from the stability of the tail, including but not limited to:
* **Global Relations:** Where the entire leading part follows a unified mathematical model, such as the **Linear Recurrence Relation** ($A_n = B \cdot A_{n-1} + C$) defined as the **Julian Class**.
* **Local Relations:** Where specific digits or subsets of digits follow their own independent patterns, such as the periodic $\{1, 6\}$ **hundreds-digit pattern** observed in the powers of $5$.

### Classification: The Julian Class
Within the family of Recurstable Numbers, those that follow a unified mathematical model are categorized as the **Julian Class**.

---

## 8.Julian’s Second Law of Recurstable Numbers
**Theorem Statement:**
A positive integer $B$ is a **Recurstable Number** if and only if its last digit $T_1 \in \{0, 1, 5, 6\}$. 

###  Mathematical Proof

To find a Recurstable Number, we only need to pass its two conditions:

1. **Terminal Stability:** Only $\{0, 1, 5, 6\}$ have a "fixed tail" when multiplied by themselves. All other digits are rejected immediately because they are unstable.

2. **Logical Leading:** The leading part $A_n$ must exhibit either Global or Local logic.
For Global Logic: As proven in Julian's First Law, the Julian Constant $C = \frac{T_1(B-1)}{10}$ must be an integer.
   * For **0 and 1**, the product $T_1(B-1)$ clearly ends in 0.
   * For **5**, $(B-1)$ is even, so $5 \times \text{even} = \dots0$.
   * For **6**, $(B-1)$ ends in 5, so $6 \times 5 = 30$.

**Conclusion:** Since $\{0, 1, 5, 6\}$ are the only digits that pass both tests, any number ending in these digits is guaranteed to be Recurstable; conversely, all Recurstable numbers must end in 0, 1, 5, or 6. 

Q.E.D.

---

## 9. Acknowledgments & Research Methodology

1. **Original Discovery & Intellectual Property Right:** The core theoretical framework and mathematical insights presented in this study are the independent discoveries of Julian Wong. This encompasses the original derivation of the $5^n$ recursive pattern and its subsequent generalization into the $\{0, 1, 5, 6\}$ terminal stability logic. As the primary investigator, Julian Wong asserts full naming rights to the following established terminology:

    * **Julian’s First Law of Recurstable Numbers** (Linear Leading Recursion)
    * **The Julian Constant ($C$)**
    * **Julian's First Law Corollary**
    * **Recurstable Numbers**
    * **The Julian Class**
   * **Julian’s Second Law of Recurstable Numbers** (The $\{0, 1, 5, 6\}$ Condition)
   
 

2. **Mathematical Guidance:** I would like to express my deepest gratitude to my mother, **Dong Cang**. She introduced me to formal algebraic methods, guiding me to use variables (such as $A_n$) and powers of ten ($10^k$) to transform my intuitive observations into a rigorous logical framework.


3. **Technical Synthesis:** As a 3rd-grade student, I adopted a collaborative approach to formalize my findings. My mother, Dong Cang, acted as my primary scribe, documenting my spoken logic and derivations. To ensure the final manuscript met international scientific standards, I utilized AI assistance to refine the academic terminology (e.g., Corollary, Terminal Stability). While the formal presentation was a collaborative effort, the mathematical discoveries and logical proofs remain my original work.
---

**License:** This project is licensed under the MIT License - see the LICENSE file for details.
