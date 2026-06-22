# Number Theory Insights

### 1. The Core: Linear Combination
* **Principle:** If $m \mid a$ and $m \mid b$, then $m \mid (as + bt)$.
* **Application:** In $a = qb + r$, the remainder $r = a - qb$ is a linear combination.
* **Conclusion:** $a, b,$ and $r$ share the same divisors, thus $\gcd(a, b) = \gcd(b, r)$.

---

### 2. Euclidean Algorithm (Two Paths)
The GCD is preserved through every reduction step:

* **Modulo (Fast):** $(a, b) \to (b, a \pmod b) \to \dots \to (\gcd, 0)$
* **Subtraction (Slow):** $(a, b) \to (a-b, b) \to \dots \to (\gcd, \gcd)$
* **Insight:** Subtraction is just a **"Slow-Motion"** version of Modulo (where $q=1$).

---

### 3. Bezout's Identity (Recursion)
* **Logic:** Since the GCD is calculated by repeatedly adding or subtracting $a$ and $b$, it must be expressible as their combination.
* **The "Recursion":** Because $d$ is calculated from Linear combination of  $a$ and $b$, you can reverse the recursion to find $s$ and $t$:
  $$d = \gcd(a, b) = as + bt$$
* **Proof of Smallest Step:** Let $a=md, b=nd$. Then $as+bt = d(ms+nt)$. 
  The **smallest positive result** is $d$ (when $ms+nt=1$), and $as+bt$ is **multiple** of $d$.

---

### 4. LCM: The Prime Logic
* **Prime Factorization:** Every composite number is a product of primes.
* **GCD:** Take maximum shared factors only once.
* **LCM:** Take **Everything**, but count shared factors only once.
* **The Common Multiple Rule:** Since any common multiple $M$ **must at least contain** all the prime product in LCM. 
* **Conclusion:** Therefore,  $M$ is a multiple of the LCM:
