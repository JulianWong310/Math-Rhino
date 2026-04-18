# Julian Carry Dynamics: The Theory of Recurstable Numbers
### *A Study on the Linear Leading-Digit Recurrence in Powers of Stable-Tail Integers*

**Author:** Julian Wong  
**Current Grade:** Grade 3 (Age 9)  
**Primary Documenter:** Dong Cang  
**Research Date:** January - April 2026  
**Location:** Mississauga, Ontario, Canada  
**Version:** v1.0.0 (Foundational Phase)  
**Keywords:** Number Theory, Power Sequences, Linear Recurrence, Stable-Tail Integers, Julian Constant ($C_J$)

---

## Foreword 
>This article began with a conversation with my 9-year-old son, Julian. One afternoon, he was excited to share his "super cool secret" about what he noticed with the powers of 5 and how the front of the numbers followed a "hidden rule."
>
>To protect his discovery and provide a solid foundation should he choose to pursue this research in the future, I have translated his ideas into standard academic language and applied for a DOI. 

---

## Abstract
This repository contains the core research for Julian Carry Dynamics, 
a new approach to number theory discovered by Julian Wong. 
The study defines Recurstable Numbers and establishes Julian's First Law, 
identifying a deterministic constant ($C_J$) that governs the leading digits of power sequences. By outlining a path toward mapping the transition from linear recurrence onto deterministic chaos, this work delivers a new structure for grasping the structural integrity of number systems.

---

## 1. What did I find?

1. For any integer exponent $n \ge 2$, the value of $5^n$ will always end in the digits **25**.
2. The hundreds digit always flips between $1$ and $6$ .
3. Let $A_n$ be the **leading digits** of $5^n$ (the number formed by removing the last two digits, $25$). 

The relationship between the current leading digits ($A_n$) and the previous leading digits ($A_{n-1}$) is defined by the formula:
$$A_n = 5A_{n-1} + 1$$

---

## 2. How did I find it? 

When you multiply the end part **25** by **5**, you get **125**. Because **$4  \times25$ = $100$**, every time you multiply by 5, it will go over 100. So:
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

## 4. The "Quinponent" Verification
* I originally named my first discovery the **"Quinponent"** pattern—a portmanteau of **Quin** (five) and **Ex-ponent**. 
* I wrote this script specifically to verify the leading digits for powers of 5.

```python
def verify_quinponent(n):
    front = 0  # Starting with 5^2
    for i in range(2, n + 1):
        result = 5**i
        print(f"5^{i} = {result} | Leading part is {front}")
        front = front * 5 + 1

if __name__ == "__main__":
    verify_quinponent(10)
```

## 5. Are there any similar numbers?
Through computational testing, I identified a class of numbers that follow the same recursive patterns as base 5.

| Tail Length ($k$) | Base ($B$) | Stable Tail ($T$) | Constant ($C$) | Recursive Formula          |
|:------------------|:-----------|:------------------|:---------------|:---------------------------|
| **1**             | 6          | 6                 | **3**          | $A_n = 6(A_{n-1}) + 3$     |
| **1**             | 36         | 6                 | **21**         | $A_n = 36(A_{n-1}) + 21$   |
| **1**             | 11         | 1                 | **1**          | $A_n = 11(A_{n-1}) + 1$    |
| **2**             | **5**      | **25**            | **1**          | $A_n = 5(A_{n-1}) + 1$     |
| **2**             | 26         | 76                | **19**         | $A_n = 26(A_{n-1}) + 19$   |
| **2**             | 45         | 25                | **11**         | $A_n = 45(A_{n-1}) + 11$   |
| **2**             | 76         | 76                | **57**         | $A_n = 76(A_{n-1}) + 57$   |
| **3**             | 25         | 625               | **15**         | $A_n = 25(A_{n-1}) + 15$   |
| **3**             | 376        | 376               | **141**        | $A_n = 376(A_{n-1}) + 141$ |
| **3**             | 425        | 625               | **265**        | $A_n = 425(A_{n-1}) + 265$ |

---

## 6. Julian's First Law of Recurstable Numbers
### 6.1 Theorem Statement:
For any base $B$ where the power $B^n$ results in a **Stable Tail ($T$)** of length $k$, the **Leading Part ($A_n$)** of the sequence can always be expressed as a linear recurrence:

$$A_n = B \cdot A_{n-1} + C_J $$

**Variable Definitions**
* **$A_n$**: The "Leading Part" of the number, calculated as the integer value remaining after removing the last $k$ digits (the stable tail).
* **$B$**: The base of the power being calculated.
* **$n$**: The exponent ($n \ge 2$).
* **$T$ :** The recurring ending value of $B^n$.
* **$k$ :** The number of digits in $T$.
* **$C_J$ (The Julian Constant)**: A fixed integer derived from the interaction between the base and the stable tail. 

**The Julian Constant Formula:**
Julian's logic dictates that the constant $C_J$ is determined by the "carry-over" from the tail's multiplication:
$$C_J = \frac{B \cdot T - T}{10^k}$$

### 6.2 Computational Verification
The following Python script puts Julian's First Law to the test.

```python
def verify_julian_first_law(B, k, max_n):
    # Calculate the Stable Tail (T)
    T = (B ** 2) % (10 ** k)
    # Calculate the Julian Constant (C_J)
    C_J = (B * T - T) // (10 ** k)

    # Starting Leading Part (A_2)
    A = (B ** 2) // (10 ** k)

    for n in range(3, max_n+1):

        # Applying Julian's First Law: A_n = B * A_{n-1} + C_J
        predict_A = B * A + C_J

        # Calculating actual value for validation
        actual_A = (B ** n) // (10 ** k)

        # Iterating: The current prediction becomes the base for the next power
        A = predict_A

        # Verify if the Law holds true
        print(f"n={n}: {predict_A == actual_A}")



if __name__ == "__main__":
    verify_julian_first_law(B=5, k=2, max_n=10)
```

---

### 6.3 Mathematical Proof
![Manuscript-01: Algebraic Derivation of CJ and First Law](https://github.com/JulianWong310/Julian-Carry-Dynamics/blob/main/2026-04-15-julian-carry-dynamics/asset/01_algebraic_derivation.png)
*Caption: My original handwritten manuscript, 
providing the formal proof of Julian’s First Law and the calculation of the Julian Constant ($C_J$).*

#### Step 1: Specific Observation (The Case of 5)

1. $5^2 = A_2 \cdot 100 + 25$
2. $5^3 = A_3 \cdot 100 + 25$
3. $\vdots$ (pattern continues...)
4. $5^{n-1} = A_{n-1} \cdot 100 + 25$
5. $5^n = A_n \cdot 100 + 25$

---

#### Step 2: Proving the Quinponent Pattern 
To find the relationship between $A_n$ and $A_{n-1}$, I used the fact that $5^n = 5^{n-1} \cdot 5$:

$$A_n \cdot 100 + 25 = (A_{n-1} \cdot 100 + 25) \cdot 5$$
$$A_n \cdot 100 + 25 = A_{n-1} \cdot 500 + 125$$
$$A_n \cdot 100 + 25 = A_{n-1} \cdot 500 + 100+25$$
$$A_n \cdot 100 + 25 = 100(A_{n-1} \cdot 5 + 1) + 25$$

By canceling the $25$ and dividing by $100$:
$$A_n = A_{n-1} \cdot 5 + 1$$

---

#### Step 3: Deriving the General Law
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

### Final Conclusion (The Core Discovery)

#### 1. **The Julian Constant:**  

   $$C_J= \frac{T \cdot B - T}{10^k}$$ 

#### 2.  **The Julian's First Law Equation:**

   $$A_n = B \cdot A_{n-1} + C_J$$

Q.E.D

---

### 6.4 Explanation: The Geometry of Interference

Mathematically, one might expect the **Leading Part ($A_n$)** to grow purely as a power function ($B^n$). However, the **Stable Tail ($T$)** introduces a persistent "interference"—the **Julian Constant ($C_J$)**.

Imagine a perfectly calm lake representing the growth of a number. Multiplying by the base should create a smooth, predictable wave. But the stable tail acts like a **small stone dropped into the water** at every step. This stone creates a ripple that shifts the Leading Part away from its original trajectory. 

The beauty of **Julian's First Law** is the discovery that this shift is not random. It is a **deterministic offset**. By identifying the Julian Constant, we have mapped the exact "ripple effect" caused by the tail, proving that what looks like a deviation is actually a perfectly fixed, rhythmic law.


### 6.4 Explanation: The Ripple Effect

You might think that the front part of a number simply grows like \(B^n\), with no extra push or pull. But the stable tail changes things.

Think of it like this:

Imagine a still lake. Dropping a stone into the water creates a ripple — a wave that spreads outward.  
Now imagine dropping a small stone **at every single step** of the sequence. That ripple never goes away. It keeps adding a tiny shift to the front part of the number.

That tiny shift is what I call the **Julian Constant (\(C_J\))**.

The surprising thing is: this shift is **not random**. It is the same every time.  
The tail acts like a steady drumbeat, and the front marches to that beat — perfectly fixed, perfectly predictable.

This is what Julian's First Law reveals: even a small, stable tail can create a lasting, repeating ripple in the front. Once you know the constant, you know the whole rhythm.

---

## 7. Julian's First Law Corollaries

### I. The Stability Requirement
According to the calculation of the Julian Constant, 
this linear recurrence exists only because the Tail (T) stays constant (stable).
If the tail were unstable, the constant ($C_J$) would become a variable, 
causing the linear structure of the Leading Part to collapse.

### II. The Integrality Guarantee
For the Linear Recurrence $A_n = B \cdot A_{n-1} + C_J$ to hold, the **Julian Constant ($C_J$)** must be an integer. We can verify this for all stable-tail bases ending in $T_1 \in \{0, 1, 5, 6\}$:

* **For 0 and 1:** The product $T_1(B-1)$ is always $0$, which is naturally divisible by $10$.
* **For 5:** Since the base $B$ ends in $5$, $(B-1)$ must be an even number. Any even number multiplied by $5$ results in a multiple of $10$.
* **For 6:** Since the base $B$ ends in $6$, $(B-1)$ must end in $5$. The product $6 \times 5 = 30$, which is also a multiple of $10$.
* **Note:** The verification above uses the case $k = 1$ (i.e., the last digit).
For k > 1, if $C_J$  is an integer then $10^k$ divides $T × (B−1)$, which implies $10$ also divides $T × (B−1)$. Hence the last‑digit condition must still hold. 

**Conclusion** — that $B$ must end in $0$, $1$, $5$, or $6$ — applies for any tail length $k$.

---

## 8. Definition & Properties of Recurstable Numbers

> *"A Recurstable Number is defined through the nature of its structure. the absolute stillness of its Tail and the consistent logic of its Head."*

### 8.1 Etymology 
The term **"Recurstable"** is an original portmanteau created by Julian Wong, synergizing **Recurrence** (the deterministic evolution of terms) and **Stable** (the invariance of terminal digits).

![Manuscript-02: Knowledge Tree of Recurstable Numbers](https://github.com/JulianWong310/Julian-Carry-Dynamics/blob/main/2026-04-15-julian-carry-dynamics/asset/02_knowledge_tree.png)
*Caption: My original knowledge map, visualizing where Julian places his original 'Recurstable Number' within the broader landscape of Number Theory.*

### 8.2 Definition
A **Recurstable Number** is a positive integer $B$ such that its power sequence $B^n$ (for $n \ge 2$) maintains an **invariant suffix** (a stable tail $T$) of length $k$. 


### 8.3 Core Properties
1. The Leading Part of a Recurstable Number follows $A_n = B \cdot A_{n-1} + C_J$.

2. A positive integer $B$ is a Recurstable Number **if and only if** its terminal digit $B \pmod{10} \in \{0, 1, 5, 6\}$. 

**Mathematical Intuition:**

* **Necessity (The DNA Test):** For a tail to be stable, the last digit must satisfy $T12≡T1(mod10)$. Testing all single digits confirms that only $0,1,5,6$ possess this natural stability.
* **Sufficiency (The Julian Link):** As established in **Corollary II**, these four digits are the only ones that guarantee the **Julian Constant ($C_J$)** is a whole number. This ensures the carry-over remains rhythmic and the linear recurrence structure never collapses.

---

## 9. Future Work: Julian Carry Dynamics

Julian Carry Dynamics is my way of watching how the front of a number changes when the back stops being simple.

The diagram below shows how I plan to explore this. I divided it into three phases based on how messy the tail is.

![Manuscript-03:Research Roadmap of Julian Carry Dynamics](./asset/IMG_1684.jpeg)
*Caption: Research roadmap. Phase I is mostly done. Phase II and III are what comes next.*


---

### Phase I: Static Stability (Low Entropy)

This is where I started. The tail does not change.

- **Single base** (like 5ⁿ):  
  Julian's First Law, Julian Constant \(C_J\), Recurstable Numbers — **done**
- **Multiple bases** (like 5ⁿ + 6ⁿ):  
  Working on it. The constant still shows up, but I am still writing the clean proof.

---

### Phase II: Dynamic Transition (Medium Entropy)

Now the tail is not fixed, but it moves in a repeating way.

Example: powers of 11. The last two digits go:  
11, 21, 31, 41, … , 01, 11, 21, … (repeats every 10 steps)

I want to ask: when the tail wiggles in a pattern, does the front wiggle along with it?  
I call this the **coupling effect**. This is my next big question.

---

### Phase III: Edge of Chaos (High Entropy)

What if the tail becomes so messy that it looks almost random?

Take powers of 3 for example.  
The last two digits of 3ⁿ go:  
03, 09, 27, 81, 43, 29, 87, 61, 83, 49, 47, 41, 23, 69, 07, 21, 63, 89, 67, 01, 03, …  
That is a long cycle (20 steps), and to a beginner it looks pretty wild.

This is not fixed (like 5ⁿ) and not super simple (like 11ⁿ).  
They live near the **Edge of Chaos**.

I want to ask: when the tail is this messy, does the front still follow any rule?  
And if it does, what is the **maximum limit** to how complicated the front can get?

Even at the edge of chaos, I believe some rules still survive.

![Manuscript-04: Phase Transition Concept](./asset/IMG_1637.jpeg)
*Caption: My first sketch of the phase transition. Low → Medium → High Entropy.*

---

### The Big Goal

I want to show that even when numbers look random, there is still hidden logic underneath.  
If that is true for numbers, maybe it is true for other things too — like weather, or heartbeats, or traffic.

That is why I keep exploring.

---

## 10. Acknowledgments & Research Methodology

1. **Intellectual Property & Naming Rights Assertion:**
The core theoretical framework and mathematical insights presented in this study are the independent discoveries of **Julian Wong**. As the primary investigator, Julian Wong claims full naming rights and intellectual priority over the following established terminology:

      * **Recurstable Numbers:** The overarching classification for integers with stable-tail power sequences.
      * **Julian’s First Law:** The linear recurrence relation $A_n = B \cdot A_{n-1} + C_J$.
      * **The Julian Constant ($C_J$):** The deterministic integer representing carry-over dynamics.
      * **The "Quinponent" Pattern:** The foundational discovery specific to powers of 5.
      * **Julian Carry Dynamics:** The prospective field investigating terminal stability as a driver for the evolution of leading numerical sequences.


2. **Mathematical Guidance:** I would like to express my deepest gratitude to my mother, **Dong Cang**. She introduced me to formal algebraic methods, guiding me to use variables (such as $A_n$) and powers of ten ($10^k$) to transform my intuitive observations into a rigorous logical framework.


3. **Technical Synthesis:** As a 3rd-grade student, I adopted a collaborative approach to formalize my findings. My mother, Dong Cang, acted as my primary scribe, documenting my spoken logic and derivations. To ensure the final manuscript met international scientific standards, I utilized AI assistance to refine the academic terminology (e.g., Corollary, Terminal Stability). While the formal presentation was a collaborative effort, the mathematical discoveries and logical proofs remain my original work.


---


**License:** This mathematical manuscript is released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
You are free to share and adapt this material for any purpose, provided you give appropriate credit to the original author: **Julian Wong**. 

*Copyright © 2026 Julian Wong. All rights reserved for original mathematical concepts and handwritten manuscripts.*