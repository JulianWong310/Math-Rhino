# 🗝️ Logic Hacker: Answer Key & Mental Models

> **Master Rule:** In competition math, the fastest way to the answer is often finding the **Constraint** (the rule that limits your options) first.

---

### 🟢 Level 1: The Divisible Code
**Question:** Smallest 3-digit integer, different digits, divisible by each of its digits.

* **Logic:** 1.  **Exclude 0:** You cannot divide by zero, so the digits cannot include 0.
    2.  **Start Small:** Test the 100s. The digits must be $\{1, 2, x\}$.
    3.  **Test 123:** $1+2+3=6$ (divisible by 3), but 123 is odd (not divisible by 2). **FAIL.**
    4.  **Test 124:** Divisible by 1 and 2. Is it divisible by 4? $24 \div 4 = 6$. **YES.** But wait—is it the smallest? 
    5.  **Test 126:** Divisible by 1 and 2. $1+2+6=9$ (not divisible by 6). **FAIL.**
    6.  **Re-check 128:** $128 \div 8 = 16$. **YES.**
* **Winner:** **128** (Note: 124 is actually smaller and works! $124/1=124, 124/2=62, 124/4=31$.)
* **Correct Answer:** **124**

---

### 🟡 Level 2: The Subset Product Hunt
**Question:** How many different numbers from multiplying 2+ members of $\{1, 2, 3, 7, 13\}$?

* **The "1" Trap:** Multiplying by 1 does not change a number ($1 \times 7 = 7$). Since we need "different" numbers from "two or more" members, we ignore 1 for a moment.
* **Logic:** All other numbers $\{2, 3, 7, 13\}$ are **Prime**. Any combination of these primes will create a unique number.
* **Counting the combinations of {2, 3, 7, 13}:**
    * Pairs (Choose 2 from 4): $\binom{4}{2} = 6$
    * Triples (Choose 3 from 4): $\binom{4}{3} = 4$
    * Quad (Choose 4 from 4): $\binom{4}{4} = 1$
    * "1": $(1, 2), (1, 3), (1, 7), (1, 13) = 4$
* **Total:** $6 + 4 + 1 +4 = 15$. 
* **Wait, what about the 1?** If you multiply $1 \times 2 \times 3$, you get 6. But we already counted $2 \times 3 = 6$. The 1 doesn't add any *new* products.
* **Answer:** **15**

---

### 🟠 Level 3: The Apartment Number Supply
**Question:** Rooms 100-115 and 300-315. How many 0-9 digit packs?

* **Logic:** Find the "Bottleneck Digit" (the one we use most).
* **Counting the '1's:**
    * **100-115:** * Hundreds place: All sixteen numbers start with '1' (**16** ones).
        * Tens place: 110, 111, 112, 113, 114, 115 (**6** ones).
        * Units place: 101, 111 (**2** ones).
        * *Total for 1st Floor:* $16 + 6 + 2 = 24$.
    * **300-315:**
        * Tens place: 310, 311, 312, 313, 314, 315 (**6** ones).
        * Units place: 301, 311 (**2** ones).
        * *Total for 2nd Floor:* $6 + 2 = 8$.
* **Grand Total:** $24 + 8 = 32$. Since each pack has only one '1', we need 32 packs.
* **Answer:** **32**

---

### 🔴 Level 4: The "Digit 8" Search
**Question:** How many two-digit integers have at least one 8?

* **Strategy: Subtraction (The Total - None Method)**
    * Total 2-digit numbers: 10 to 99 (**90** numbers).
    * Numbers with NO 8s: 
        * Tens place: 8 choices (1, 2, 3, 4, 5, 6, 7, 9).
        * Units place: 9 choices (0, 1, 2, 3, 4, 5, 6, 7, 9).
        * $8 \times 9 = 72$.
    * Total - No 8s: $90 - 72 = 18$.
* **Answer:** **18**

---

### 🟣 Level 5: The Prime Product Challenge
**Question:** How many factors of 30 are in the set of products of distinct prime factors of 210?

* **Logic:**
    1.  Prime factors of $210 = 2 \times 3 \times 5 \times 7$.
    2.  Factors of $30 = \{1, 2, 3, 5, 6, 10, 15, 30\}$.
    3.  Can we make each factor using $\{2, 3, 5, 7\}$?
        * 1: (The empty product or "multiplying zero members" - in math contests, we usually check if 1 is allowed).
        * 2, 3, 5: Yes (single members).
        * 6 ($2 \times 3$), 10 ($2 \times 5$), 15 ($3 \times 5$), 30 ($2 \times 3 \times 5$): Yes.
* **Answer:** **8** (If the problem allows 1 as a product of "zero" primes, otherwise 7).
