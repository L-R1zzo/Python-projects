# 🔃 Selection Sort — Python Implementation
 
A selection sort algorithm implemented from scratch in Python, without using any built-in sorting functions.
 
## 📌 What is Selection Sort?
 
Selection sort works by repeatedly finding the smallest element in the unsorted portion of the list and swapping it into its correct position. At each iteration, the sorted portion grows by one element until the entire list is ordered.
 
## ⚙️ How It Works
 
```
Initial:  [64, 25, 12, 22, 11]
 
Step 1 → minimum = 11 → swap with 64 → [11, 25, 12, 22, 64]
Step 2 → minimum = 12 → swap with 25 → [11, 12, 25, 22, 64]
Step 3 → minimum = 22 → swap with 25 → [11, 12, 22, 25, 64]
Step 4 → minimum = 25 → already in place → [11, 12, 22, 25, 64]
Step 5 → minimum = 64 → already in place → [11, 12, 22, 25, 64] ✓
```
 
At each step, the algorithm scans the unsorted portion, finds the minimum, and swaps it into position.
 
## 📊 Time Complexity
 
| Case | Complexity |
|---|---|
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |
 
Unlike other sorting algorithms, selection sort always performs O(n²) comparisons regardless of the input — even if the list is already sorted. This makes it inefficient for large datasets but simple to understand and implement.
 
## 🚀 Usage
 
```python
numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))
# [11, 12, 22, 25, 64]
 
print(selection_sort([1]))
# [1]
 
print(selection_sort([3, 1, 2]))
# [1, 2, 3]
```
 
## 📚 Concepts Covered
 
- Nested loops and index tracking
- In-place swapping with tuple unpacking
- Comparison-based sorting
- O(n²) time complexity
## 🛠️ Tech
 
- Python 3
- No external libraries
 
