# The Magic of GCD & Linear Combinations

### 1. Bézout's Identity (Theorem 1)
* **The Rule:** For any integers $a$ and $b$, there exist integers $s$ and $t$ such that:
    $$as + bt = \gcd(a, b)=d$$
#### The Core Logic: Why $d = as + bt$?

The reason this works is rooted in the **Subtraction Method**. Since we find the Greatest Common Divisor ($d$) by repeatedly subtracting $a$ and $b$ from each other, we can simply "undo" or reverse those steps. 

By backtracking through each subtraction, we can rewrite the final $d$ as a combination of our original building blocks, $a$ and $b$.


---

####  Quick Proof (Example: $a=10, b=6$)
We use the subtraction steps to "track" the variables:

1.  **Step 1:** Find 4.  
    $4 = a - b$
2.  **Step 2:** Find 2 (The GCD).  
    $2 = b - 4$
3.  **Step 3:** Substitute Step 1 into Step 2:  
    $2 = b - (a - b)$  
    $2 = 2b - a$  *(This is our Linear Combination!)*

---
### 🔄 Is it Recursion? (The GCD Logic)

In programming, the **Extended Euclidean Algorithm** (Bézout's Identity) is a perfect example of recursion:

1. **The Call (Going Down):** Keep calling the function with smaller numbers until you hit the base case (the GCD).
   *Example:* `gcd(10, 6)` -> `gcd(6, 4)` -> `gcd(4, 2)`

2. **The Return (The Reverse):** This is where you **backtrack**. You take the result and "unfold" it to find $s$ and $t$.
   *Example:* `2 = 6 - 4` -> replace 4 with `(10 - 6)`...

**Conclusion:** Bézout's Identity is exactly the **Return/Reverse** phase of the GCD recursion!

---

###  2 The Universal Rule: Bézout's Lemma

Beyond just finding the GCD, the formula $as + bt$ tells us something about **every** number we can possibly create using $a$ and $b$:

* **The Multiple Rule:** Any integer that can be written in the form $as + bt$ **must** be a multiple of $\gcd(a, b)$.
* **The Set of Reachable Numbers:** If you combine $a$ and $b$ in any way ($as + bt$), the result will always be in the set:
    $$\{ \dots, -2d, -d, 0, d, 2d, \dots \}$$
    *(where $d = \gcd(a, b)$)*

---

#### Why is $as + bt$ always a multiple of $d$?

This is the "Inheritance" logic:
1.  Since $d$ is a divisor of $a$, then $a$ is a multiple of $d$ (e.g., $a = m \cdot d$).
2.  Since $d$ is a divisor of $b$, then $b$ is a multiple of $d$ (e.g., $b = n \cdot d$).
3.  Substitute these into the combination:
    $$as + bt = (md)s + (nd)t = d(ms + nt)$$
4. **Final Conclusions:**

* **Rule A (The Multiple):** Any combination $as + bt$ must be a **multiple** of $d$.
* **Rule B (The Minimum):** The **smallest** positive result of $as + bt$ is $d$ (when $ms + nt = 1$).

$$as + bt = d(1) = d$$

---


#### 🪣 The Water Bucket Analogy
Imagine you have two water buckets: one holds **$a$** liters and the other holds **$b$** liters. 

The **GCD** is the smallest positive amount of water you can possibly measure using these two buckets. By pouring water back and forth (which is just adding or subtracting bucket volumes), you are guaranteed to be able to measure out exactly **$d$** liters.


### ✍️ Practice 

#### Q1: The Possible Measurement (21L & 15L)
**Questions:**
1. What is the $\gcd(21, 15)$?
2. Can you measure out exactly **3 liters**?
3. Can you measure out exactly **10 liters**?

**Answers:**
1. **$\gcd = 3$**. (Factors of 21: 1, 3, 7, 21; Factors of 15: 1, 3, 5, 15).
2. **Yes**. Since 3 is the $\gcd$, it is the "smallest unit" we can measure ($21 - 15 = 3$).
3. **No**. Because 10 is **not** a multiple of 3. You can only measure amounts on the "3-grid" ($3, 6, 9, 12 \dots$).

---

#### Q2: Building the Recipe ($a=5, b=3$)
**Questions:**
1. Find the $\gcd(5, 3)$.
2. Write down the subtraction steps to get to the $\gcd$.
3. Backtrack those steps to find $s$ and $t$ so that $5s + 3t = \gcd$.

**🔑Answers:**
1. **$\gcd = 1$**. (5 and 3 are prime to each other).
2. **Subtraction Steps:**
   - Step 1: $5 - 3 = \mathbf{2}$
   - Step 2: $3 - 2 = \mathbf{1}$ (This is our $\gcd$)
3. **Backtracking:**
   - From Step 2: $1 = 3 - \mathbf{2}$
   - Replace the '2' using Step 1: $1 = 3 - (5 - 3)$
   - Simplify: $1 = 3 - 5 + 3 \Rightarrow \mathbf{1 = 2(3) - 1(5)}$
   - **Result:** $s = -1, t = 2$.

---
