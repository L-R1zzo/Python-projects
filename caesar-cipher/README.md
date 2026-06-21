# Caesar Cipher 🔐

A command-line tool to encrypt and decrypt messages using the Caesar cipher — one of the oldest encryption techniques in history.

---

## How it works

The Caesar cipher shifts each letter of the alphabet by a fixed number of positions. With a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on. To decrypt, the shift is simply reversed.

```
hello  →  (shift 3)  →  khoor
khoor  →  (shift 3)  →  hello
```

---

## Getting started

No external libraries needed — just Python 3.

```bash
git clone https://github.com/Rizzo-08/Caesar-cipher.git
cd Caesar-cipher
python caesar.py
```

---

## Usage

Run the script and follow the prompts:

```
Do you want to encrypt or decrypt?
> encrypt

What is the message? --THE CIPHER ONLY WORKS WITH ALPHABET'S CHARACTERS--
> hello world

With which shift?
> 3

khoor zruog
```

```
Do you want to encrypt or decrypt?
> decrypt

What is the message?
> khoor zruog

With which shift?
> 3

hello world
```

---

## Notes

- Works with both uppercase and lowercase letters
- Non-alphabet characters (spaces, numbers, punctuation) are preserved as-is
- Shift must be an integer between 1 and 25

---

## Project structure

```
Caesar-cipher/
├── caesar.py   # Core logic + CLI
└── README.md
```

---

## Built with

- Python 3
