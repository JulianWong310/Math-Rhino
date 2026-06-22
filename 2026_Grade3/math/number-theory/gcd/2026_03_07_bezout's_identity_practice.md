# 🏆 Bézout's Identity & GCD Advanced Practice

*Instructions: This set focuses on the core logic of Bézout's Identity: an equation $ax + by = c$ has integer solutions if and only if $\gcd(a, b)$ divides $c$.*

---

## 📝 Practice Questions (New Set)

### 1. The Smallest Measurement
You have two unmarked buckets with capacities of **24 liters** and **60 liters**. By filling, pouring, and emptying them, what is the **smallest positive integer** amount of water you can measure exactly?
* (A) 4  
* (B) 6  
* (C) 12  
* (D) 24  
* (E) 2  

### 2. Logical Exclusion
Given integers $a$ and $b$ such that $\gcd(a, b) = 13$. Which of the following values **CANNOT** be a result of the linear combination $ax + by$?
* (A) 13  
* (B) 26  
* (C) 39  
* (D) 50  
* (E) 130  

### 3. Power of Coprimality
If $a$ and $b$ are two **coprime** positive integers, what is true about the integer solutions for the equation $ax + by = 5$?
* (A) It must have solutions.  
* (B) It must have no solutions.  
* (C) It only has solutions if $a=5$ or $b=5$.  
* (D) It only has solutions if $a+b=5$.  
* (E) It depends on whether $a$ and $b$ are odd.  

### 4. Robot Landing Points
A robot starts at point 0 on a number line. It can only jump **21 units** to the right or **15 units** to the left. Which of the following coordinates **CANNOT** be reached by the robot?
* (A) 3  
* (B) 6  
* (C) 10  
* (D) 15  
* (E) 21  



### 5. Coefficient Matching
It is known that $\gcd(17, 5) = 1$. If we write the linear combination $17x + 5y = 1$, which of the following pairs $(x, y)$ is an integer solution?
* (A) $(1, -3)$  
* (B) $(2, -7)$  
* (C) $(-2, 7)$  
* (D) $(3, -10)$  
* (E) $(-1, 4)$  

### 6. Smallest Element of a Set
Let $S$ be the set of all integers that can be written as $36s + 48t$ for any integers $s$ and $t$. What is the **smallest positive integer** in set $S$?
* (A) 1  
* (B) 6  
* (C) 12  
* (D) 24  
* (E) 36  

### 7. Constraints on GCD
If the equation $as + bt = 20$ has integer solutions, and $d = \gcd(a, b)$, which statement about $d$ must be true?
* (A) $d = 20$  
* (B) $d$ is a divisor of 20.  
* (C) $d$ is a multiple of 20.  
* (D) $d$ must be a prime number.  
* (E) $d$ must be greater than 20.  

### 8. Contest Scoring Logic
In a competition, there are two ways to score points: Move A earns **14 points** and Move B earns **35 points**. Which of the following total scores is **impossible** for an athlete to achieve exactly?
* (A) 7  
* (B) 21  
* (C) 49  
* (D) 50  
* (E) 70  

### 9. Multiple Property
If $10s + 15t = K$ holds for some integers $s$ and $t$, then $K$ must satisfy which condition?
* (A) $K$ must be even.  
* (B) $K$ must be a multiple of 5.  
* (C) $K$ must be a multiple of 10.  
* (D) $K$ must be a multiple of 15.  
* (E) $K$ must be a multiple of 25.  

### 10. Ultimate Scaling Property
Given $d = \gcd(a, b)$, and $sa + tb = d$. If we multiply both $a$ and $b$ by 3, what is the new smallest positive linear combination result?
* (A) $d$  
* (B) $3d$  
* (C) $d/3$  
* (D) $9d$  
* (E) It remains the same.  

---

## 🔑 Answer Key & Logic Analysis

| Q# | Ans | Core Logic | Explanation |
| :--- | :--- | :--- | :--- |
| 1 | **(C)** | $\gcd(24, 60)$ | The GCD of 24 and 60 is 12. |
| 2 | **(D)** | $d \mid (ax+by)$ | All results must be multiples of 13; 50 is not. |
| 3 | **(A)** | $1 \mid c$ | Coprime means $d=1$. Since 1 divides 5, solutions exist. |
| 4 | **(C)** | $\gcd(21, 15)$ | $\gcd(21, 15) = 3$. Coordinates must be multiples of 3. 10 is not. |
| 5 | **(C)** | Substitution | $17(-2) + 5(7) = -34 + 35 = 1$. |
| 6 | **(C)** | Bézout's Definition | The smallest positive integer in the set is $\gcd(36, 48) = 12$. |
| 7 | **(B)** | Divisibility | $d$ must be a divisor of the constant on the right side (20). |
| 8 | **(D)** | $\gcd(14, 35)$ | $\gcd(14, 35) = 7$. Scores must be multiples of 7. 50 is not. |
| 9 | **(B)** | Common Divisor | $\gcd(10, 15) = 5$, so $K$ must be a multiple of 5. |
| 10 | **(B)** | Homogeneity | $\gcd(3a, 3b) = 3 \times \gcd(a, b) = 3d$. |