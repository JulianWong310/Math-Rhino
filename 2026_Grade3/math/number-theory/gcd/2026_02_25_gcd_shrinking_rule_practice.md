

## ✍️ Shrinking Rule Focus

**Q1. Logic Check** If $126 = 30 \times 4 + 6$, according to the Shrinking Rule, which is true?  
A) $(126, 30) = (126, 6)$  
B) $(126, 30) = (30, 6)$  
C) $(126, 30) = (4, 6)$  
D) $(126, 30) = (30, 4)$  

**Q2. The Zero Property** What is the value of $GCD(0, -25)$?  
A) 0  
B) -25  
C) 25  
D) 1  

**Q3. Consecutive Integers** For any positive integer $n$, what is the $GCD(n, n+1)$?  
A) 1  
B) $n$  
C) $n+1$  
D) 2  

**Q4. Property Application** To find $GCD(48, 18)$, we write $48 = 18 \times 2 + 12$. What is the next step?  
A) Find $GCD(48, 12)$  
B) Find $GCD(18, 2)$  
C) Find $GCD(18, 12)$  
D) Find $GCD(12, 2)$  

**Q5. Variables Challenge** Find the $GCD(2n+1, n)$ using the Shrinking Rule.  
A) $n$  
B) 1  
C) 2  
D) $2n$  

**Q6. The "Combo" Logic** If $d|a$ and $d|b$, why must $d$ divide $c = a - 3b$?  
A) Because $c$ is a linear combination of $a$ and $b$  
B) Because $d$ is a prime number  
C) Because $a$ and $b$ are coprime  
D) Because $c$ is smaller than $a$  

**Q7. Group vs. Pair** In the group $\{6, 10, 15\}$, which statement is true?  
A) The group is not coprime because $GCD(6, 10, 15) \neq 1$  
B) Every pair in the group is coprime  
C) The group is coprime, but no pair inside is coprime  
D) The GCD of the group is 5  

**Q8. Absolute Value** If $GCD(x, y) = 15$, what is $GCD(|x|, |-y|)$?  
A) -15  
B) 15  
C) 0  
D) 30  

**Q9. Big Number Shrink** Using the rule $(a, b) = (b, c)$, simplify $GCD(100, 70)$. The first step is:  
A) $(70, 30)$  
B) $(100, 30)$  
C) $(70, 10)$  
D) $(30, 10)$  

**Q10. Coding Logic** Julian's Python code uses `a, b = b, a % b` in a loop. Which rule is this?  
A) The Absolute Value Rule  
B) The Coprime Trap  
C) The Shrinking Rule (Euclidean Algorithm)  
D) The Zero Property  

---

## 🔑 Answer Key & Explanations

| Question | Answer | Explanation |
|:---------| :--- | :--- |
| **Q1**   | **B** | The rule states $(a, b) = (b, c)$, where $b$ is the divisor and $c$ is the remainder. |
| **Q2**   | **C** | $GCD(0, b) = \|b\|$. So $GCD(0, -25) = \|-25\| = 25$. |
| **Q3**   | **A** | Using the rule: $(n+1, n) = (n, 1)$. The GCD of any number and 1 is always 1. |
| **Q4**   | **C** | In the next step of the Euclidean Algorithm, the old divisor (18) becomes the new dividend, and the remainder (12) becomes the new divisor. |
| **Q5**   | **B** | $(2n+1) = n \times 2 + 1$. So $GCD(2n+1, n) = GCD(n, 1) = 1$. |
| **Q6**   | **A** | This is the "Combo Rule" (Rule 3). Since $c = 1a + (-3)b$, any $d$ that divides $a$ and $b$ must divide $c$. |
| **Q7**   | **C** | $GCD(6,10,15)=1$ (Coprime), but $GCD(6,10)=2$, $GCD(10,15)=5$, and $GCD(6,15)=3$. None are coprime! |
| **Q8**   | **B** | GCD is always the same for absolute values: $(x, y) = (\|x\|, \|y\|)$. |
| **Q9**   | **A** | $100 = 70 \times 1 + 30$. The rule $(a, b) = (b, c)$ results in $(70, 30)$. |
| **Q10**  | **C** | The Python operator `%` gives the remainder $c$. This loop is the standard Euclidean Algorithm. |

---

