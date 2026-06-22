# 🧮 The Ultimate Divisibility Master List
**Topic:** Shortcuts for Mental Math & Coding
**Date:** February 18, 2026
---

### 1. The Basic Rules
| Number | The Rule | Example                  |
| :--- | :--- |:-------------------------|
| **2** | Last digit is even ($0, 2, 4, 6, 8$). | $128$ ✅                  |
| **3** | The **sum of all digits** is divisible by 3. | $123$ ($1+2+3=6$) ✅      |
| **4** | The **last two digits** are divisible by 4. | $512$ ✅                  |
| **5** | Last digit is $0$ or $5$. | $95$ ✅                   |
| **6** | Pass both the **Rule for 2** AND **Rule for 3**. | $18$ (Even + Sum is 9) ✅ |
| **8** | The **last three digits** are divisible by 8. | $1,048$ ✅                |
| **9** | The **sum of all digits** is divisible by 9. | $729$ ($7+2+9=18$) ✅     |
| **10** | Ends in $0$. | $500$ ✅                  |

---

### 2. The "Contest Math" Rules (7, 11, 13, 17, 19)
These are the tricks used in math competitions to solve problems fast.

#### **The 7 Rule (Double and Subtract)**
* **How:** Double the last digit and subtract it from the rest.
* **Test 392:** $2 \times 2 = 4$. $39 - 4 = 35$. Since $7|35$, then **$7|392$**.

#### **The 11 Rule (The Wave)**
* **How:** Alternate adding and subtracting digits from left to right.
* **Test 2728:** $2 - 7 + 2 - 8 = -11$. Since $-11$ is divisible by 11, then **$11|2728$**.

#### **The 13 Rule (4x and Add)**
* **How:** Multiply the last digit by **4** and add it to the rest.
* **Test 169:** $9 \times 4 = 36$. $16 + 36 = 52$. Since $13 \times 4 = 52$, then **$13|169$**.

#### **The 17 Rule (5x and Subtract)**
* **How:** Multiply the last digit by **5** and subtract it from the rest.
* **Test 221:** $1 \times 5 = 5$. $22 - 5 = 17$. Since $17|17$, then **$17|221$**.

#### **The 19 Rule (2x and Add)**
* **How:** Double the last digit and add it to the rest.
* **Test 361:** $1 \times 2 = 2$. $36 + 2 = 38$. Since $19 \times 2 = 38$, then **$19|361$**.

---
# 🧮 Divisibility Challenge: The "Secret Codes"
**Topic:** Primes & Logic (7, 11, 13, 17, 19)
---
### Part 1: Mental Math Shortcuts
*Use the rules we learned to solve these. Don't use a calculator!*

**Q1. The 7 Test (Double & Subtract)**
Is **553** divisible by 7?  
* *Action:* $55 - (3 \times 2) = ?$
* *Answer:* [ ] Yes / [ ] No

**Q2. The 11 Test (The Wave)**
Is **3,817** divisible by 11?  
* *Action:* $3 - 8 + 1 - 7 = ?$
* *Answer:* [ ] Yes / [ ] No

**Q3. The 13 Test (4x & Add)**
Is **299** divisible by 13?  
* *Action:* $29 + (9 \times 4) = ?$
* *Answer:* [ ] Yes / [ ] No

**Q4. The 17 Test (5x & Subtract)**
Is **459** divisible by 17?  
* *Action:* $45 - (9 \times 5) = ?$
* *Answer:* [ ] Yes / [ ] No

**Q5. The 19 Test (2x & Add)**
Is **437** divisible by 19?  
* *Action:* $43 + (7 \times 2) = ?$
* *Answer:* [ ] Yes / [ ] No

---

### Part 2: Logic & Python Coding
*Think like a computer scientist.*

**Q6. The "6" Logic Gate**
To pass the "6" test, a number must be divisible by both **2** and **3**.  
Which of these numbers passes the test?
* A) 122
* B) 123
* C) 126

**Q7. The "15" Logic Gate**
In Python: `if n % 3 == 0 and n % 5 == 0:`  
Which of these values for `n` would make the computer say **True**?
* A) 10
* B) 45
* C) 25

**Q8. The "9" vs "3" Mystery**
If the sum of a number's digits is **15**:
* Is it divisible by 3? [ ] Yes / [ ] No
* Is it divisible by 9? [ ] Yes / [ ] No

---

### 🐍 Python Pro-Tip
If you want to check these in Python, you don't need the tricks! Just use the **Modulo Operator `%`**:

```python
# Checking for 19
number = 361
if number % 19 == 0:
    print("19 divides it perfectly!")
   ```

