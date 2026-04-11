# Julian's First Law and the World of Recurstable Numbers
**By: Julian Wong (Grade 3)** 

Hi! I am a 3rd grade student. While exploring the powers of 5 today, I discovered a super cool secret hidden within the numbers. I am naming this discovery the 'Julian's First Law' and calling these types of integers 'Recurstable Numbers.



---

##  What did I find?

1. For any integer exponent $n \ge 2$, the value of $5^n$ will always end in the digits **25**.
2. The hundreds digit always flips between $1$ and $6$ .
3. Let $A_n$ be the **leading digits** of $5^n$ (the number formed by removing the last two digits, $25$). 

The relationship between the current leading digits ($A_n$) and the previous leading digits ($A_{n-1}$) is defined by the formula:
$$A_n = 5(A_{n-1}) + 1$$

---

##  How did I find it? 

I figured it out! When you multiply the end part (**25**) by **5**, you get **125**. 

Because **$4  \times25$ = $100$**, every time you multiply by 5, it will go over 100. So:
- The **$25$** stays at the end.
- The **$1$** always **"carry over"** to the next place (the hundreds place).

That’s why you take the previous leading part, multiply it by 5, and then **always add 1**! This also explains the **1-6 Flip-Flop**:
- If the front ends in **1**: $1 \times 5 + 1 = \mathbf{6}$
- If the front ends in **6**: $6 \times 5 + 1 = 3\mathbf{1}$ (it goes back to 1!)

---

##  Let's see it in action:

| Power ($5^n$) | Result | leading Part ($A_n$) | Calculation ($5 \cdot A_{n-1} + 1$) | **1-6 Pattern** |
| :--- | :--- |:---------------------| :--- | :--- |
| $5^2$ | 25 | 0                    | (Base Case) | - |
| $5^3$ | 125 | **1**                | $5(0) + 1 = 1$ | **1** |
| $5^4$ | 625 | **6**                | $5(1) + 1 = 6$ | **6** |
| $5^5$ | 3125 | 3**1**               | $5(6) + 1 = 31$ | **1** |
| $5^6$ | 15625 | 15**6**              | $5(31) + 1 = 156$ | **6** |


---

##  The "Quinponent" Verification
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

##  Are there any similar numbers?

| Order ($k$) | Base ($B$) | Stable Tail ($T$) | Julian Constant ($C$) | Recursive Formula |
| :--- | :--- | :--- | :--- | :--- |
| **1** | 6 | 6 | **3** | $A_n = 6(A_{n-1}) + 3$ |
| **1** | 11 | 1 | **1** | $A_n = 11(A_{n-1}) + 1$ |
| **2** | **5** | **25** | **1** | $A_n = 5(A_{n-1}) + 1$ |
| **2** | 25 | 25 | **6** | $A_n = 25(A_{n-1}) + 6$ |
| **2** | 26 | 76 | **19** | $A_n = 26(A_{n-1}) + 19$ |
| **2** | 45 | 25 | **11** | $A_n = 45(A_{n-1}) + 11$ |
| **2** | 76 | 76 | **57** | $A_n = 76(A_{n-1}) + 57$ |
| **3** | 25 | 625 | **15** | $A_n = 25(A_{n-1}) + 15$ |
| **3** | 376 | 376 | **141** | $A_n = 376(A_{n-1}) + 141$ |
| **3** | 425 | 625 | **265** | $A_n = 425(A_{n-1}) + 265$ |


---

## Recurstable Numbers: The Core Concept

### Etymology 
The term **"Recurstable"** is a portmanteau created by me, combining **Recursion** and **Stable**.

### Definition
A Recurstable Number is a positive integer $B$ that satisfies two conditions for $n \geq 2$:
1. **Terminal Stability (The Tail):** The last $k$ digits ($T$) remain constant.
2. **Leading-Digit Recursion (The Head):** The leading digits $A_n$ follow a linear recurrence:
$$A_n = B(A_{n-1}) + C$$

---

##  Julian's Second Law: The Law of Units-Digit Stability

### 1. The Hypothesis
Through independent logical reasoning, I concluded that a Recurstable Number ($B$) must end in **0, 1, 5, or 6**. 

### 2. The Logic 
My reasoning is based on the "Self-Multiplication" property. For any number to maintain a stable tail throughout its powers, the very last digit must be able to "survive" the multiplication without changing.

If you multiply a digit by itself:
* **5 times 5** ends in **5**
* **6 times 6** ends in **6**
* **1 times 1** ends in **1**
* **0 times 0** ends in **0**

If we picked a number like **4**, $4 \times 4 = 16$. The tail has already changed from a 4 to a 6. Once the units digit changes, the stability of the entire tail is broken. Therefore, only the set **{0, 1, 5, 6}** can ever be the seed for a Recurstable Number.

---

## Julian's First Law: The General Formula

### Step 1: Specific Observation (The Case of 5)
(To describe this for any power, I used the algebraic notation taught by my mother to write the formulas for $n$ and $n-1$):
I started by looking at the powers of 5 and splitting them into a "Head" ($A_n$) and a "Tail" ($25$):

1. $5^2 = A_2 \cdot 100 + 25$
2. $5^3 = A_3 \cdot 100 + 25$
3. $\vdots$
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
$$A_n = B \cdot A_{n-1} + \frac{T \cdot B - T}{10^k}$$

---

### Step 4: Final Conclusion (The Core Discovery)

1.  **The Julian Constant:** The "secret" number that controls the growth of the head is:
    $$C = \frac{T \cdot B - T}{10^k}$$

2.  **The Julian's First Law Equation:**
    $$A_n = B \cdot A_{n-1} + C$$

3.  **Principle of Stability:** This linear pattern only works because the Tail ($T$) is **Stable**. If the tail were not stable, the constant $C$ would break, and the pattern would disappear!

---

##  Acknowledgments & Research Methodology

This research is a collaborative effort involving original discovery, educational guidance, and technical synthesis:

1. **Original Discovery:** The $5^n$ pattern, the $\{0, 1, 5, 6\}$ logic, and the naming of "Recurstable Numbers" are the independent work of Julian Wong.
2. **Mathematical Guidance:** I would like to express my deepest gratitude to my **Mother**. She introduced me to formal algebraic methods, teaching me how to use variables (like $A_n$) and powers of ten ($10^k$) to transform my observations into a logical proof.
3. **Technical Synthesis:** As I am a 3rd-grade student, I utilized **AI assistance** to translate my ideas into formal English and to provide the precise academic terminology used throughout this document. This assisted in articulating my findings to meet international scientific documentation standards.

---

*License:* This project is licensed under the MIT License - see the LICENSE file for details.
