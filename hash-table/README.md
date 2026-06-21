# 🗂️ Hash Table — Python Implementation
 
A hash table implemented from scratch in Python, without using any built-in hash map libraries. Built to understand how data structures work under the hood.
 
## 📌 What is a Hash Table?
 
A hash table stores **key-value pairs** using a hashing function to compute an index for each key. This allows for near-constant time `O(1)` lookups, insertions, and deletions on average.
 
## ⚙️ How It Works
 
1. A **key** is passed to the `hash()` method
2. The hash is computed as the **sum of Unicode values** of each character in the key
3. The resulting integer is used as the index in the internal `collection` dictionary
4. **Collisions** (multiple keys producing the same hash) are handled via **chaining** — all colliding pairs are stored together in a nested dictionary under the same hash index
```
hash("golf") → 103 + 111 + 108 + 102 = 424
 
collection = {
    424: { "golf": "sport" }
}
 
# Collision example: "fcc" and "cfc" produce the same hash
collection = {
    300: { "fcc": "coding", "cfc": "chemical" }
}
```
 
## 🧰 Methods
 
| Method | Description |
|---|---|
| `hash(key)` | Returns the sum of Unicode values of each character in the key |
| `add(key, value)` | Inserts a key-value pair into the table, handles collisions |
| `remove(key)` | Removes a key-value pair safely, does nothing if the key doesn't exist |
| `lookup(key)` | Returns the value associated with the key, or `None` if not found |
 
## 🚀 Usage
 
```python
ht = HashTable()
 
ht.add("golf", "sport")
ht.add("fcc", "coding")
ht.add("cfc", "chemical")  # collides with "fcc"
 
print(ht.collection)
# { 424: { "golf": "sport" }, 300: { "fcc": "coding", "cfc": "chemical" } }
 
ht.lookup("golf")   # "sport"
ht.lookup("cfc")    # "chemical"
ht.lookup("xyz")    # None
 
ht.remove("fcc")
print(ht.collection)
# { 424: { "golf": "sport" }, 300: { "cfc": "chemical" } }
```
 
## 📚 Concepts Covered
 
- Abstract Data Types (ADT)
- Hashing and hash functions
- Collision resolution via chaining
- Time complexity: `O(1)` average, `O(n)` worst case
## 🛠️ Tech
 
- Python 3
- No external libraries
