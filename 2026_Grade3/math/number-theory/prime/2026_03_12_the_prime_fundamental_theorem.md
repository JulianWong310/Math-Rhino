# 📔 The Magic of Prime Bricks


### ⭐ Theorem 3: The Fundamental Theorem of Arithmetic (Most Important)

**Standard Factorization Theorem for Integers**
Any integer $a > 1, a \in \mathbb{Z}^+$ can be factored into a product of primes, and this factorization is unique.
There exist primes $p_1 \le p_2 \le \dots \le p_n$ such that:
$$a = p_1 p_2 \dots p_n$$


**Logic:**
Every number is built from special Prime Bricks!

Think of **Prime Numbers** (2, 3, 5, 7...) as the basic Lego pieces that you **cannot** break or snap apart. Every other number is just a building made from these pieces.

**1. You can build any number:**
If you have enough Prime Bricks, you can build any number in the world.
* $12 = 2 \times 2 \times 3$
* $30 = 2 \times 3 \times 5$



**2. The Recipe is Unique:**
Every number has its own **Secret Recipe**. 
If you build the number 30 using one 2, one 3, and one 5, there is **no other way** to do it. You can't use different prime bricks to get 30. It's like a number's DNA!

---

### 🖇️ How to use the "Secret Recipe"

#### Rule 1: Finding the GCD (The Sharing Rule)
If two numbers want to share their bricks, the **GCD** is just the bricks they **both** have in their pockets (the ones they share).

* **Number A has:** [2, 2, 5]
* **Number B has:** [2, 5, 5]
* **They both have:** One [2] and one [5].
* **GCD:** $2 \times 5 = 10$.



#### Rule 2: Finding the LCM (The All-In Rule)
The **LCM** is the **smallest collection of bricks** you need to be able to build **either** Number A **or** Number B. You don't want to buy extra bricks, so you **overlap** the ones they share!

* **Number A needs:** [2, 2, 5]
* **Number B needs:** [2, 5, 5]
* **Your All-In Toolkit:**
    1.  Start with A's bricks: **[2, 2, 5]**
    2.  Check what B needs: B needs a [2] (we already have it!), and **two** [5]s. We only have one [5], so we add **one more [5]**.
* **Toolkit (LCM):** [2, 2, 5, 5]
* **LCM:** $2 \times 2 \times 5 \times 5 = 100$.

> **Summary:**
> * **GCD** = Only the bricks in the **overlap**.
> * **LCM** = **All** the bricks from both, but you only count the **overlap** once!

---

#### Rule: Perfect Squares (The Pair Rule)
A number is a **Perfect Square** (like 4, 9, 16) ONLY if every prime brick in its recipe has a **twin brother**.
* $36 = (2 \times 2) \times (3 \times 3)$ -> Every brick has a pair! ✅
* $12 = (2 \times 2) \times 3$ -> The 3 is lonely! So 12 is NOT a perfect square. ❌

---

### ♾️ Theorem 4: The Never-Ending Prime Factory
**There are INFINITELY many prime numbers!**

How do we prove it? Let’s play a game:

Imagine you think you have found **ALL** the prime bricks in the world: **{2, 3, 5}**.

**Step 1: Build the Giant Tower (Multiply them)**
Multiply all your primes together:
$$2 \times 3 \times 5 = 30$$
*This tower is perfectly divisible by 2, 3, and 5.*

**Step 2: Add 1 to the Tower**
Now, make the tower one layer taller:
$$30 + 1 = 31$$

**Step 3: The Magic Remainder**
If you try to divide this new number (31) by any of your original bricks, look what happens:
* **Divide by 2:** $31 \div 2 = 15 \dots \text{remainder } 1$
* **Divide by 3:** $31 \div 3 = 10 \dots \text{remainder } 1$
* **Divide by 5:** $31 \div 5 = 6 \dots \text{remainder } 1$

### 🧐 What does this mean?
Because there is **always a remainder of 1**, none of your original bricks (2, 3, 5) are "factors" of 31.

According to **Theorem 3**, every number must be made of prime bricks. So, for the number 31, there are only two choices:
1.  **31 is a new Prime Brick** itself (which is true!).
2.  **31 is made of other Prime Bricks** that were not in your bag (like 7, 11, 13...).

**Conclusion:** No matter how many primes you find, you can always use this trick to find another one. They never, ever end!


----


### 🏆 Mini-Detective practice

**1. Which number is a "Prime Brick" (you can't break it)?**
* (A) 4 (It breaks into 2x2)
* (B) 7
* (C) 9 (It breaks into 3x3)

**2. If Number A is $2 \times 3$ and Number B is $2 \times 5$, what brick do they share?**
* (A) 2
* (B) 3
* (C) 5

**3. Will we ever run out of Prime Numbers?**
* (A) Yes, when we reach a billion.
* (B) No, they go on forever!