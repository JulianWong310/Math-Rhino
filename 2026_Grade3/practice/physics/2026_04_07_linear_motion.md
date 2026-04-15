# Linear Motion
> **Topic:** Understanding Speed, Distance, and Time ($v = s/t$)

---

## 1. Core Concepts (The Lecture)

### A. How do we compare speed?
To determine how fast an object moves, we use two primary methods:
1.  **Fixed Time:** Compare the distance covered. (More distance = Faster)
2.  **Fixed Distance:** Compare the time taken. (Less time = Faster)

### B. Defining Speed ($v$)
In physics, **Speed** is the ratio of distance traveled to the time taken.

**The Formula:**
$$v = \frac{s}{t}$$

*   **$s$**: Distance (Meters - m)
*   **$t$**: Time (Seconds - s)
*   **$v$**: Speed (Meters per second - m/s)

### C. Unit Conversions
While the SI unit is **m/s**, we often use **km/h** in daily life (like car speedometers).
*   **The Golden Ratio:** $1 \text{ m/s} = 3.6 \text{ km/h}$
* **Example:** $10 \text{ m/s} = 36 \text{ km/h}$
### D. Unit Conversions: The "3.6" Secret
While the SI unit is **m/s**, we often use **km/h** in daily life. Here is how we get the conversion factor:

### The Derivation
1. **Distance:** $1 \text{ km} = 1,000 \text{ m}$
2. **Time:** $1 \text{ hour} = 60 \text{ min} \times 60 \text{ sec} = 3,600 \text{ s}$

By substituting these into the fraction:
$$\frac{1 \text{ km}}{1 \text{ h}} = \frac{1,000 \text{ m}}{3,600 \text{ s}} = \frac{1 \text{ m}}{3.6 \text{ s}}$$

**Therefore:**
* To go from **m/s → km/h**: Multiply by **3.6**
* To go from **km/h → m/s**: Divide by **3.6**


---

## 2. Types of Motion

| Type | Definition | Feature |
| :--- | :--- | :--- |
| **Uniform Rectilinear** | Moving in a straight line at a constant speed. | Speed never changes. |
| **Variable Motion** | Speed changes during the journey. | Requires calculating **Average Speed**. |

> **Note on Average Speed:** 
> When calculating average speed for a trip (like the train from Beijing to Shanghai), you must use the **total distance** divided by the **total time**, including any stops made at stations.

---

## 3. Practice Problems 

### Task 1: The Walker
A person walks **4.5 km** in **45 minutes**. 
*   **Q1:** Calculate the speed in km/h.
*   **Q2:** Convert that speed to m/s.

### Task 2: The High-Speed Railway (HSR)
Based on the Beijing-Shanghai timetable:
*   **Total Mileage:** 1318 km
*   **Total Duration:** 4 hours 38 minutes
*   **Goal:** Calculate the average speed of the entire journey.

---

## 4. Answer Key (Results)

### Solution for Task 1:
* **Step 1 (km/h):** Convert 45 min to hours $\rightarrow$ $45 / 60 = 0.75 \text{ h}$.
  $v = 4.5 \text{ km} / 0.75 \text{ h} = \mathbf{6 \text{ km/h}}$
* **Step 2 (m/s):** $6 / 3.6 = \mathbf{1.67 \text{ m/s}}$

### Solution for Task 2:
* **Step 1 (Time):** 4 hours 38 minutes = $4 + (38/60) \approx 4.633 \text{ hours}$.
* **Step 2 (Speed):** $v = 1318 \text{ km} / 4.633 \text{ h} \approx \mathbf{284.5 \text{ km/h}}$

---

## 4. PyCharm Python Lab 🐍

Copy this code into a file named `motion_calc.py` in PyCharm to verify your homework answers.

```python
def calculate_velocity(distance_km, time_minutes):
    # Convert minutes to hours
    time_hours = time_minutes / 60
    
    # Calculate speed in km/h
    v_kmh = distance_km / time_hours
    
    # Convert km/h to m/s (Divide by 3.6)
    v_ms = v_kmh / 3.6
    
    return round(v_kmh, 2), round(v_ms, 2)

# Test with Task 1
dist = 4.5
t_min = 45
kmh, ms = calculate_velocity(dist, t_min)

print(f"--- Julian's Physics Lab ---")
print(f"Distance: {dist} km")
print(f"Speed: {kmh} km/h")
print(f"Speed: {ms} m/s")