# 🧮 Number Systems
**Topic:** The Clans of Numbers
**Date:** February 17, 2026
---

## 1. The Number "Clans" (Sets)
In Math, we group numbers into "Clans" (Sets). In Python, we call these **Types**.

* **$\mathbb{N}$ — Natural Numbers:** The "Counting Numbers" (e.g., $1, 2, 3 \dots$).
* **$\mathbb{W}$ — Whole Numbers:** Natural numbers PLUS Zero (e.g.,$0, 1, 2, 3\dots$).
* **$\mathbb{Z}$ — Integers:** The "Whole Family." Includes positives, negatives, and **Zero** (e.g., $-2, -1, 0, 1, 2\dots$).
    > **Python Language:** We call these `int`.
* **$\mathbb{Q}$ — Rational Numbers:** Any number that can be written as a **fraction** (like $1/2$ or $0.75$).
* **$\mathbb{R}$ — Real Numbers:** Every number on the number line, including "messy" numbers like $\pi$ ($3.14159...$).
    > **Python Language:** We call these `float`.



---

## 2. The Secret Symbols (Math vs. Python)
To read the "Black Book" (AoPS), you need to translate these symbols. Here is your cheat sheet:

| Math Symbol | Meaning | Python Equivalent |
| :--- | :--- | :--- |
| **$q$** | **Quotient** (The whole result of division) | `//` (Floor Division) |
| **$r$** | **Remainder** (What is left over) | `%` (Modulo) |
| **$\in$** | **Belongs to** (Is a member of a clan) | `isinstance(x, int)` |
| **$\forall$** | **For All** (A rule for everyone) | `for item in list:` |
| **$\exists$** | **There Exists** (At least one) | `if some_condition:` |

---

## 3. The "Closure" Rule (The Secret Circle)
A set is **"Closed"** if you do math with two members of the clan, and the result **stays** in that same clan.

* **Addition (+):** Integers are **CLOSED**.  
  * *Proof:* $5 + (-2) = 3$. (Integer + Integer = Integer).
* **Division ($\div$):** Integers are **NOT CLOSED**.  
  * *Proof:* $1 \div 2 = 0.5$. (0.5 is a `float`, so it jumped out of the Integer Clan!).

---

## ✍️ Practice Challenges 

**Q1. The Clan Hunt** In Python, if you type `print(10 / 2)`, the computer says `5.0`.  
Based on that `.0`, which Clan does the result belong to?  
* **A)** $\mathbb{Z}$ (Integers)  
* **B)** $\mathbb{Q}$ (Rational/Float)

**Q2. The Translator** Translate this "Black Book" sentence into English:  
**$\forall$ x in N, x < 0**

**Q3. The Odd Clan Mystery** Imagine a Clan of only **ODD numbers** $\{1, 3, 5, 7, \dots\}$.  
Is this Clan **Closed** under **Addition**?  
*(Try it: 1 + 3 = ? Is the answer still an Odd number?)*

**Q4. The Python Code Trick** * If `number % 2 == 0` is True, is the number **Even** or **Odd**?  
* If `number % 10 == 0` is True, what digit does the number **always** end with?

---
