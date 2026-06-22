# Merge Sort: Divide and Conquer 🧩

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Sorting-emerald)
![Style](https://img.shields.io/badge/Approach-In--Place--Mutation-orange)

An elegant, stable, and predictable implementation of the **Merge Sort algorithm** in Python, leveraging the classic **Divide and Conquer** paradigm.

Unlike QuickSort, which picks a pivot to partition data, Merge Sort blindly splits the array exactly down the middle, recursively sorts the halves, and then performs a highly efficient **merge** operation to reconstruct the sorted array.

---

## 🧠 How it Works: Split & Merge

Merge Sort operates in two distinct phases:
1. **Divide (Top-Down):** The unsorted list is iteratively split into halves until we reach sub-lists containing a single element (which are inherently sorted).
2. **Conquer/Merge (Bottom-Up):** The algorithm steps back up the recursion tree, merging two sorted sub-lists into a single, combined sorted list by comparing front elements.

```text
               Divide: [4, 10, 6, 14, 2, 1, 8, 5]
                             /            \
               [4, 10, 6, 14]              [2, 1, 8, 5]
                 /        \                  /        \
             [4, 10]    [6, 14]          [2, 1]      [8, 5]
              /   \      /   \            /   \       /   \
            [4]  [10]  [6]  [14]        [2]  [1]    [8]  [5]
             \    /     \    /           \    /      \    /
 Conquered:  [4, 10]    [6, 14]          [1, 2]      [5, 8]
                 \        /                  \        /
               [4, 6, 10, 14]              [1, 2, 5, 8]
                             \            /
               Merge:  [1, 2, 4, 5, 6, 8, 10, 14]
