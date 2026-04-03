# 🏆 Arrangements and Factorial Magic

---

## 📝 Part 1: The Challenges

### **Q1. The Pokémon Parade**
Julian has **4 different Pokémon** figurines. He wants to arrange all of them in a single row on his desk. How many different arrangements are possible?
* (A) 4  
* (B) 10  
* (C) 16  
* (D) 24  

### **Q2. The Mario Kart Podium**
In a Mario Kart race with **8 racers**, how many different ways can the **Top 3** (1st, 2nd, and 3rd place) be decided?
* (A) 24  
* (B) 120  
* (C) 336  
* (D) 504  

### **Q3. The Chess Piece Line-up**
Julian wants to place a **King, a Queen, a Rook, a Bishop, and a Knight** in a row on the first rank of the board. How many different ways can he order these 5 pieces?
* (A) 25  
* (B) 60  
* (C) 120  
* (D) 720  

### **Q4. The Three-Letter Word (New!)**
How many different 3-letter "words" (they don't have to be real words) can be made using the letters in **"MATH"** if each letter can be used **at most once**?
* (A) 4  
* (B) 12  
* (C) 24  
* (D) 64  

### **Q5. The Small Club Election**
A math club has **5 members**. They need to elect one President and one Vice-President. How many different pairs of leaders are possible?
* (A) 5  
* (B) 10  
* (C) 20  
* (D) 25  

### **Q6. The Pokémon Party Choice**
Julian has **6 Pokémon** in his backpack. He needs to choose **only 2** of them to stand in a line for a battle (where the first one is the "Lead" and the second is the "Backup"). How many different Lead-Backup pairs can he make?
* (A) 12  
* (B) 30  
* (C) 36  
* (D) 720  

### **Q7. The Password Rule**
How many different 3-digit security codes can be made using the digits {1, 2, 3, 4, 5} if **no digit can be repeated**?
* (A) 15  
* (B) 60  
* (C) 120  
* (D) 125  

### **Q8. The Zero Magic**
What is the value of $3! + 0!$?
* (A) 3  
* (B) 4  
* (C) 6  
* (D) 7  

### **Q9. The Team Photo**
Julian and his **5 friends** (6 people in total) are taking a photo. Julian insists on standing at the **far left** of the row. How many ways can the other 5 friends stand in the remaining spots?
* (A) 120  
* (B) 720  
* (C) 5040  
* (D) 6  

### **Q10. The Big Race**
In a race with **10 runners**, how many ways can the **Gold, Silver, and Bronze** medals be awarded?
* (A) 30  
* (B) 120  
* (C) 720  
* (D) 5040  

---

## 🗝️ Part 2: Answer Key

| Question | Answer | Factorial / Counting Logic |
| :--- | :--- | :--- |
| **Q1** | **(D) 24** | $4! = 4 \times 3 \times 2 \times 1$ |
| **Q2** | **(C) 336** | $8 \times 7 \times 6$ (Stop after 3 spots) |
| **Q3** | **(C) 120** | $5! = 5 \times 4 \times 3 \times 2 \times 1$ |
| **Q4** | **(C) 24** | $4 \times 3 \times 2$ (4 choices for 1st letter, then 3, then 2) |
| **Q5** | **(C) 20** | $5 \times 4$ (2 spots to fill) |
| **Q6** | **(B) 30** | $6 \times 5$ (2 spots to fill) |
| **Q7** | **(B) 60** | $5 \times 4 \times 3$ (3 spots, no repeats) |
| **Q8** | **(D) 7** | $3! = 6$ and $0! = 1$, so $6 + 1 = 7$ |
| **Q9** | **(A) 120** | Julian is fixed (1 way), others are $5!$ |
| **Q10** | **(C) 720** | $10 \times 9 \times 8$ |

---

## 💻 Part 3: Python Verification Script

```python
import math

# Julian, you can verify Q4 (The MATH word) like this:
letters = ['M', 'A', 'T', 'H']
count = 0
for first in letters:
    for second in letters:
        if second == first: continue
        for third in letters:
            if third == first or third == second: continue
            count += 1
print(f"Q4 Answer: {count}")

# Verify Q9: If Julian is fixed at the start, only 5 people move.
q9_result = math.factorial(5)
print(f"Q9 Answer: {q9_result}")