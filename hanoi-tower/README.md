# 🗼 Tower of Hanoi Solver

A recursive implementation in **Python** of the classic mathematical puzzle, the **Tower of Hanoi**. 

Unlike standard solvers that only output text instructions (e.g., *"Move disk from A to C"*), this script **visually tracks and prints the actual physical state of the three rods at every single step**, making the call stack flow incredibly easy to follow.

## 📋 Table of Contents
- [The Problem](#-the-problem)
- [Algorithm Logic](#-algorithm-logic)
- [Source Code](#-source-code)
- [Output Example](#-output-example)

---

## 🧩 The Problem
The Tower of Hanoi is a puzzle consisting of three rods and $N$ disks of decreasing size. The objective is to move the entire stack from the starting rod to the target rod, obeying three strict rules:
1. Only **one disk** can be moved at a time.
2. You can only move the **topmost disk** of a rod.
3. **No disk may ever be placed on top of a smaller disk**.

---

## 🧠 Algorithm Logic
The solution relies on the recursive **Divide and Conquer** principle. To move $N$ disks from `source` to `destination` using a `pivot` rod:

1. **Step 1:** Recursively move the top $N-1$ disks from `source` to `pivot`.
2. **Step 2:** Move the remaining largest disk directly from `source` to `destination`.
3. **Step 3:** Recursively move the $N-1$ disks sitting on the `pivot` onto the largest disk on `destination`.

The base case occurs when $N = 1$, where the single remaining disk is moved immediately.

---

## 💻 Source Code

```python
def hanoi_solver(disks: int):
    # The 3 fixed physical rods
    first_road = list(range(1, disks + 1))[::-1]
    second_road = []
    third_road = []
    moves = []
    
    # Recursive core (rod roles shift at each level of the stack)
    def hanoi(disks, source, destination, pivot):
        if disks == 1:
            destination.append(source.pop())
            moves.append(f"{first_road} {second_road} {third_road}")
            return

        hanoi(disks - 1, source, pivot, destination)
        
        destination.append(source.pop())
        moves.append(f"{first_road} {second_road} {third_road}")
        
        hanoi(disks - 1, pivot, destination, source)

    # Capture initial state and trigger recursion
    moves.append(f"{first_road} {second_road} {third_road}")
    hanoi(disks, first_road, third_road, second_road)
    
    return "\n".join(moves)

if __name__ == "__main__":
    print(hanoi_solver(3))
```

---

## 📊 Output Example (3 Disks)

The integers represent the disk size (`3` being the largest at the bottom, `1` being the smallest at the top):

```text
[3, 2, 1] [] []         <-- Initial State (All disks on Rod 1)
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]           <-- The largest disk (3) hits the target rod
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]         <-- Final State (Solved!)
```
