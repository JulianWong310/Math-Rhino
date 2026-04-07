# 🏆 Challenge 2: Solutions & Logic Guide

## Level 1: The Prime Mirror (The "7" Trap)
**The Answer:** **89**

* **Logic:** An **Emirp** is a prime that is still prime when digits are reversed (e.g., $17 \leftrightarrow 71$).
* **The Search:**
    * **97:** Prime $\rightarrow$ Reverse is $79$ (Prime). **Verdict: Emirp.**
    * **91:** **"The Fake Prime"** ($7 \times 13 = 91$). **Verdict: Not a Prime.**
    * **89:** Prime $\rightarrow$ Reverse is $98$ (Even). **Verdict: NOT an Emirp.**
* **Conclusion:** **89** is the largest two-digit prime that fails the mirror test.

---

## Level 2: Factorial DNA Cleanup
**The Answer:** $N + 2$

**The Algebraic Breakdown:**
1.  **Expand the numerator:** $(N+2)! = (N+2) \times (N+1) \times N!$
2.  **Substitute into fraction:**
    $$\frac{(N+2) \times (N+1) \times N!}{N! \times (N+1)}$$
3.  **Cancel common terms:**
    * $N!$ on top and bottom $\rightarrow$ **Cancel.**
    * $(N+1)$ on top and bottom $\rightarrow$ **Cancel.**
4.  **Final Result:** $N + 2$

---

## Level 3: The "Plus One" Equation
**The Answer:** $n = 4$

**The Step-by-Step Logic:**
1.  **Factor out $n!$:** $n! \cdot (n + 1) = 120$
2.  **Simplify:** By definition, $n! \cdot (n + 1)$ is $(n+1)!$.
3.  **Find the Factorial:** We know $5! = 120$ ($5 \times 4 \times 3 \times 2 \times 1$).
4.  **Solve for $n$:** If $(n+1)! = 5!$, then $n+1 = 5$, which means **$n = 4$**.

---

## Level 4: The Square Factor Hunt (6!)
**The Answer:** **144**

**The Calculation:**
1.  **$6! = 720$**.
2.  **Prime Factorization:** $2^4 \times 3^2 \times 5^1$.
3.  **Find the Perfect Square:** To get the *greatest* square, we take all even exponents: $2^4 \times 3^2$.
4.  **Result:** $16 \times 9 = \mathbf{144}$ (which is $12^2$).

---

## Level 5: Narcissistic Numbers (The "Cubes")
**The Answer:** **153, 370, 371, 407**

**Mathematical Proof:**
* $153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27$
* $370 = 3^3 + 7^3 + 0^3 = 27 + 343 + 0$
* $371 = 3^3 + 7^3 + 1^3 = 27 + 343 + 1$
* $407 = 4^3 + 0^3 + 7^3 = 64 + 0 + 343$

---

## Level 6: The "B-C" License Plate
**The Answer:** **300,000**

**The Logic:**
* **Slot 1 (Letters):** 3 options (B, C, or D).
* **Slots 2-6 (Digits):** 10 options per slot ($0-9$).
* **Calculation:** $3 \times 10 \times 10 \times 10 \times 10 \times 10 = \mathbf{300,000}$ possible IDs.

---

## Level 7: The Rival Captains (No-Together Rule)
**The Answer:** **16**

**The "Subtraction Hack" Strategy:**
1.  **Total Ways:** $\binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20$.
2.  **Illegal Teams:** (Alex + Ben + 1 other). Since 2 spots are already taken, we pick 1 more from the remaining 4 friends. $\binom{4}{1} = 4$.
3.  **Final Result:** $20 - 4 = \mathbf{16}$ valid teams.
