# 📐 Square Root — Bisection Method
 
A square root calculator implemented from scratch in Python using the **bisection method**, without relying on `math.sqrt()` or any external library.
 
## 📌 What is the Bisection Method?
 
The bisection method finds the square root of a number by narrowing down an interval where the root must lie, halving it at each step until the result is within an acceptable margin of error (tolerance).
 
It works on the same principle as binary search — instead of scanning linearly, it eliminates half the search space at every iteration.
 
## ⚙️ How It Works
 
To find √x, we look for a value `mid` such that `mid² ≈ x`:
 
```
Target: √25
 
low = 0, high = 25
Step 1 → mid = 12.5  → 12.5²  = 156.25 > 25 → high = 12.5
Step 2 → mid = 6.25  → 6.25²  = 39.06  > 25 → high = 6.25
Step 3 → mid = 3.125 → 3.125² = 9.76   < 25 → low  = 3.125
Step 4 → mid = 4.687 → 4.687² = 21.97  < 25 → low  = 4.687
...
Step N → mid = 5.0   → 5.0²   = 25.0   ✓
```
 
### Key insight for small numbers (x < 1)
 
For numbers smaller than 1, the square root is **larger** than the number itself:
 
```
√0.001 = 0.0316...  but  0.001 < 0.0316
```
 
So the interval is set as `low = x²` instead of `0`, which places the starting point much closer to the actual root and allows convergence in fewer iterations.
 
## 🚀 Usage
 
```python
square_root_bisection(25)
# The square root of 25 is approximately 5.0
 
square_root_bisection(0.001, 1e-7, 50)
# The square root of 0.001 is approximately 0.031622776601683794
 
square_root_bisection(0)
# The square root of 0 is 0
 
square_root_bisection(-4)
# ValueError: Square root of negative number is not defined in real numbers
 
square_root_bisection(225, 1e-7, 10)
# Failed to converge within 10 iterations
```
 
## 🧰 Parameters
 
| Parameter | Description | Default |
|---|---|---|
| `x` | The number to find the square root of | required |
| `tolerance` | Acceptable margin of error | `0.01` |
| `max_iterations` | Maximum number of bisection steps | `1000` |
 
## 📊 Time Complexity
 
| Case | Complexity |
|---|---|
| Average | O(log n) |
| Worst | O(log n) |
 
Each iteration halves the search space, so convergence is logarithmic — the same as binary search.
 
## 📚 Concepts Covered
 
- Bisection method / binary search applied to mathematics
- Interval narrowing and convergence
- Tolerance and precision control
- Edge case handling (negative numbers, 0, 1, small decimals)
## 🛠️ Tech
 
- Python 3
- No external libraries
