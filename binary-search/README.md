# 🔍 Binary Search — Python Implementation
 
A binary search algorithm implemented from scratch in Python, with path tracking to visualize how the search narrows down the target.
 
## 📌 What is Binary Search?
 
Binary search is an efficient algorithm for finding an element in a **sorted list**. Instead of scanning every element one by one, it repeatedly halves the search space until the target is found.
 
## ⚙️ How It Works
 
```
Target: 37
List: [2, 5, 8, 12, 16, 23, 37, 44, 56, 72, 91]
 
Step 1 → middle = 23 → 37 > 23 → search right half
Step 2 → middle = 56 → 37 < 56 → search left half
Step 3 → middle = 44 → 37 < 44 → search left half
Step 4 → middle = 37 → found!
```
 
Instead of checking all 11 elements, it found the target in **4 steps**.
 
## 📊 Time Complexity
 
| Case | Complexity |
|---|---|
| Average | O(log n) |
| Worst | O(log n) |
| Best | O(1) |
 
With 1,000,000 elements, binary search needs at most **20 steps**. A linear search would need up to 1,000,000.
 
## 🚀 Usage
 
```python
numbers = list(range(1000001))
 
print(binary_search(numbers, 656340))
# [500000, 750000, 625000, 562500, 593750, 609375, 632812, 644531, 650390, 653320, 654785, 655517, 655883, 656066, 656158, 656294, 656339, 656362, 656350, 656344, 656341, 656340]
# Value found at index 656340
```
 
## ⚠️ Requirements
 
The input list **must be sorted**. Binary search does not work on unsorted lists.
 
## 🛠️ Tech
 
- Python 3
- No external libraries
 
