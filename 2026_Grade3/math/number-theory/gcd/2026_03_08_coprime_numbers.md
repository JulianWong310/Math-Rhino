# 🎓 The Secret of Coprime Numbers

### 1. Bézout's Identity (Theorem 1)
* **The Rule:** For any integers $a$ and $b$, there exist integers $s$ and $t$ such that:
    $$as + bt = \gcd(a, b)$$
* **Special Case:** If $\gcd(a, b) = 1$, then $as + bt = 1$.
* **The Converse:** If you can find integers $s$ and $t$ such that $as + bt = 1$, then $\gcd(a, b)$ **must** be 1.

    
>**Example B:** $a=3, b=5$  
>   $\gcd(3, 5) = 1$  
>   **Combination:** $3(2) + 5(-1) = 1$
---



### 2. The Casting Out Rule (Theorem 2)
**Rule:** If $\gcd(a, c) = 1$, then $\gcd(ab, c) = \gcd(b, c)$.

**Why? (Linear Combination Logic):**
* We have $as + ct = 1$.
* Multiply by $b$: $(ab)s + c(bt) = b$.
* Since $b$ is a **linear combination** of $ab$ and $c$, they share the same common divisors!

> **Example:** $a=5, c=3, b=12$.
> * $\gcd(5 \times 12, 3) = \gcd(60, 3) = 3$.
> * $\gcd(12, 3) = 3$.
> * **Result:** Both are 3! ✅

---

### 3. Euclid's Lemma (Corollary)
**Rule:** If $\gcd(a, c) = 1$ and $c \mid ab$, then $c \mid b$.

**Proof:**
1. From Theorem 2, we know $\gcd(ab, c) = \gcd(b, c)$.
2. If $c \mid ab$, then $\gcd(ab, c) = c$.
3. Substitute: $c = \gcd(b, c)$.
4. Therefore, $c \mid b$. 

> **Example:** $a=7, c=9, b=18$.
> * $\gcd(7, 9) = 1$. 
> * Since $9 \mid (7 \times 18)$, then $9$ MUST divide $18$. ✅

---

### 4: Practice

#### Task 1: Mental Math
If $\gcd(101, 3) = 1$, what is $\gcd(101 \times 6, 3)$? 
*(Hint: Just cast out the 101!)*

#### Task 2: Linear Combination Challenge
Can you find $s, t$ for $2s + 5t = 1$?


#### Task 3: Python Lab
```python
import math

def casting_out_test(a, b, c):
    if math.gcd(a, c) == 1:
        res1 = math.gcd(a * b, c)
        res2 = math.gcd(b, c)
        print(f"Ignore {a}: gcd({a}*{b}, {c}) is {res1}. gcd({b}, {c}) is {res2}. Match!")

# Try this:
casting_out_test(13, 10, 7)