# 🏆 The Master's Logic: GCD & Coprimality

## 1. Fundamental Properties (The Basics)
* **The Zero Case:** $\gcd(a, 0) = |a|$
    * *Logic:* Every number divides 0, so the Greatest Common Divisor is $a$ itself.
* **Associative Property:** $\gcd(a, b, c) = \gcd(\gcd(a, b), c) = \gcd(a, \gcd(b, c))$
    * *Logic:* You can calculate the GCD of a list by pairing them up in any order.
* **Linear Combination Rule:** $\gcd(a, b) \mid (ax + by)$
    * *Logic:* The GCD of two numbers must divide any linear combination of those numbers.

---

## 2. Scaling & Reduction (The Simplifiers)
* **Scaling Up:** $\gcd(ka, kb) = k \cdot \gcd(a, b)$
    * *Example:* $\gcd(30, 42) = 6 \cdot \gcd(5, 7) = 6$.
* **Scaling Down:** If $\gcd(a, b) = d$, then $\gcd(\frac{a}{d}, \frac{b}{d}) = 1$
    * *Logic:* After dividing both numbers by their GCD, the remaining parts are always **Coprime**.
* **The "Stranger" Rule:** If $\gcd(a, c) = 1$, then $\gcd(ab, c) = \gcd(b, c)$
    * *Logic:* If $a$ and $c$ share no factors, $a$ has no influence on the GCD of $b$ and $c$.

---

## 3. Euclidean Algorithm: the Efficiency Shortcuts 
* **Subtraction Method** $\gcd(a, b) = \gcd(a \pm b, b)$
* **Modulo Method:** $\gcd(a, b) = \gcd(a - kb, b)$ for any integer $k$
    * *Logic:* This is the heart of the Euclidean Algorithm. You can add or subtract multiples of one number from the other without changing the GCD.
    * *Example:* $\gcd(n+1, 2n+3) = \gcd(n+1, (2n+3) - 2(n+1)) = \gcd(n+1, 1) = 1$.

---

## 4. Coprime Rules (Relatively Prime)
Two numbers $a$ and $b$ are coprime if $\gcd(a, b) = 1$.
* **Consecutive Integers:** $\gcd(n, n+1) = 1$
    * *Rule:* Any two numbers next to each other are always coprime.
* **Consecutive Odd Integers:** $\gcd(2n-1, 2n+1) = 1$
* **Prime Power Rule:** If $p$ is prime and $p \nmid a$, then $\gcd(a, p) = 1$.
* **Product Rule:** If $\gcd(a, c) = 1$ and $\gcd(b, c) = 1$, then $\gcd(ab, c) = 1$.

---

## 5. The Ultimate Weapon: Bézout's Identity
* **The Identity:** There exist integers $s$ and $t$ such that gcd(a, b)$=$as + bt. 
**as+bt** is multiple of gcd(a,b) and gcd(a,b) is the smallest positive number.
* **Coprime Test:** $\gcd(a, b) = 1 \iff ax + by = 1$ has integer solutions.
    * *Tip:* If you can find a way to add/subtract $a$ and $b$ to get 1, you've instantly proven they are coprime!

---

# 📝Practice: Logic & Computation

**Problem 1: The Stranger Danger** Given $\gcd(x, 11) = 1$. Simplify $\gcd(77x, 11)$.  
*(Hint: Use the "Stranger" Rule and Scaling Up)*

**Problem 2: The Variable Eraser** Simplify $\gcd(n + 5, 2n + 11)$.  
*(Hint: Try to subtract $2 \times (n+5)$ from the second term)*

**Problem 3: The Scaling Trick** If $\gcd(a, b) = 10$, what is the value of $\gcd(3a, 3b)$?

**Problem 4: Proof by Bézout** Find a combination of $3n + 1$ and $n$ that equals $1$. Does this prove they are coprime?  
*(Example: $(3n+1) - 3(n) = ?$)*

**Problem 5: Multiple Numbers** Find $\gcd(12, 18, 30)$ using the **Associative Property**.

---

# 🔑 Answer Key

| Problem | Answer | Master's Logic |
| :--- | :--- | :--- |
| **1** | **11** | $\gcd(77x, 11) = 11 \cdot \gcd(7x, 1)$. Since $\gcd(x, 11)=1$, only 11 remains. |
| **2** | **1** | $\gcd(n+5, (2n+11) - 2(n+5)) = \gcd(n+5, 1) = 1$. |
| **3** | **30** | Using Scaling Up: $3 \cdot \gcd(a, b) = 3 \cdot 10 = 30$. |
| **4** | **Yes, 1** | $(3n+1) - 3n = 1$. Since $ax+by=1$, they are coprime ($\gcd=1$). |
| **5** | **6** | $\gcd(12, 18) = 6$. Then $\gcd(6, 30) = 6$. |