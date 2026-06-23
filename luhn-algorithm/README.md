# 💳 Luhn Algorithm — Python Implementation
 
A credit card number validator implemented from scratch in Python using the Luhn algorithm, without relying on any external library.
 
## 📌 What is the Luhn Algorithm?
 
The Luhn algorithm is a simple checksum formula used to validate identification numbers — most commonly credit card numbers. It doesn't verify whether a card actually exists, but it does catch common input errors like mistyped digits.
 
It is used by Visa, Mastercard, American Express, and virtually every major payment processor in the world.
 
## ⚙️ How It Works
 
```
Card number: 4539 5783 4338 3949
 
Step 1 → remove spaces and dashes → 4539578343383949
Step 2 → reverse the digits      → 9493383343875354
Step 3 → double every second digit (index 1, 3, 5...):
 
9  4  9  3  3  8  3  3  4  3  8  7  5  3  5  4
   ↑     ↑     ↑     ↑     ↑     ↑     ↑     ↑
   8     6    16     6     6    14     6     8  ← doubled
 
Step 4 → if doubled value > 9, subtract 9:
16 → 7
14 → 5
 
Step 5 → sum all digits → total
Step 6 → if total % 10 == 0 → VALID ✓
```
 
## 🚀 Usage
 
```python
print(verify_card_number("4539 5783 4338 3949"))  # VALID!
print(verify_card_number("1234 5678 9012 3456"))  # INVALID!
print(verify_card_number("4539-5783-4338-3949"))  # VALID! (handles dashes too)
```
 
## 📚 Concepts Covered
 
- String manipulation and cleaning
- List indexing and reversal
- Modular arithmetic
- Checksum validation
## 🛠️ Tech
 
- Python 3
- No external libraries
 
