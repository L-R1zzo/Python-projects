# QuickSort: 3-Way Partitioning (Dutch National Flag) 🚀

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Sorting-emerald)
![License](https://img.shields.io/badge/license-MIT-green)

A clean, highly readable, and Pythonic implementation of the **QuickSort algorithm** utilizing **3-Way Partitioning** (also known as the *Dutch National Flag problem*, formulated by Edsger Dijkstra).

Unlike standard QuickSort implementations that split an array into two halves, this approach divides the data into **three distinct partitions** relative to a chosen `pivot`.

---

## 🧠 The "Why": Standard vs. 3-Way QuickSort

In a classic 2-way QuickSort, if an array contains many duplicate values (e.g., `[4, 1, 4, 4, 2, 4, 3]`), the algorithm redundantly sends those identical values down into the recursion stack. This can cause the time complexity to severely degrade from $O(n \log n)$ down to **$O(n^2)$**.

**3-Way Partitioning solves this:** By grouping all elements equal to the pivot into an `equals` bucket, the algorithm isolates them and **never touches them again**. If an array consists entirely of identical numbers, this QuickSort sorts it in **$O(n)$** linear time at the very first pass.

```text
               Input: [20, 3, 14, 20, 1, 5, 20]   (Pivot: 20)
                                 │
           ┌─────────────────────┼─────────────────────┐
           ▼                     ▼                     ▼
       [ minors ]            [ equals ]            [ majors ]
      [3, 14, 1, 5]         [20, 20, 20]              [ ]
           │                     │                     │
      quick_sort()          (Skipped!)            quick_sort()
           │                     │                     │
           └─────────────────────┼─────────────────────┘
                                 ▼
                     Result: [1, 3, 5, 14, 20, 20, 20]
