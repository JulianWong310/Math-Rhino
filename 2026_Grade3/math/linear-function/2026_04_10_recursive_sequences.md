<div align="center">

## Recursive Sequences

</div>


### Part 1: Reviewing Your "Quinponent Theorem"

In math, we use $n$ to represent the step (the exponent) and $A_n$ to represent the **Leading Digits** of that step.
Your magic formula is:
$$A_n = 5(A_{n-1}) + 1$$

#### **Question 1: Validating the Base**
We know that $5^4 = 625$, so $A_4 = 6$. Use your formula to find the leading digits for $5^5$ ($A_5$).
* **Your Calculation:** ____________________
* **Answer:** $A_5 =$ __________

#### **Question 2: The Source of the 1-6 Pattern**
You noticed the hundreds digit (the last digit of the front part) flips between 1 and 6. Let's calculate:
* If $A_{n-1}$ ends in **1** $\rightarrow$ the next is $5 \times 1 + 1 =$ **( ? )**
* If $A_{n-1}$ ends in **6** $\rightarrow$ the next is $5 \times 6 + 1 =$ **( ? )**
* **Conclusion:** This is why the hundreds digit ____________________.

---

### Part 2: The "Function Machine" Challenge

A function is like a machine: you give it an **Input**, and it follows a rule to give you an **Output**. 
Let’s turn your rule into a machine named $f(x)$:
$$f(x) = 5x + 1$$

#### **Question 3: Operating the Machine**
If I drop the number **156** (which is the front part of $5^6$) into this machine, what number will pop out?
* **Result:** __________

#### **Question 4: Reverse Thinking**
If the machine pops out the number **1**, what number did I drop in as the Input?
* **Hint:** What number times 5, plus 1, equals 1?
* **Answer:** __________

---

### Part 3: Branching Out (High School Sequences)

Julian, let's try a brand-new "Magic Machine" rule!
Suppose the new rule is: **Next Number = (Previous Number $\times$ 2) + 3**.
The math formula looks like this:
$$a_n = 2a_{n-1} + 3$$

##### **Question 5: The New Rule Challenge**
If the first number in this sequence is $a_1 = 1$, find the next numbers:
1.  $a_2 = 2 \times (1) + 3 =$ __________
2.  $a_3 = 2 \times (\text{answer from above}) + 3 =$ __________
3.  $a_4 = 2 \times (\text{answer from above}) + 3 =$ __________

##### **Question 6: The Ultimate Discovery**
Look at the sequence you just created: $1, 5, 13, 29, \dots$
Do you see a pattern in the **last digit** (the ones place)? Which numbers is it flipping between?
* **My Discovery:** The last digit flips between __________ and __________!

---
