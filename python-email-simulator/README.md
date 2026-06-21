# 📧 Python Email Simulator

A simple email system simulation built with Python, using Object-Oriented Programming (OOP) principles.

## 📌 Description

This project simulates a basic email client where users can send, read, and delete emails. It was built to practice OOP concepts such as classes, methods, and object interactions.

## 🚀 Features

- Send emails between users
- View inbox with read/unread status
- Read full email content
- Delete emails from inbox

## 🗂️ Project Structure

```
python-email-simulator/
│
├── email_simulator.py   # Main source file
└── README.md
```

## ⚙️ How to Run

Make sure you have Python 3 installed, then run:

```bash
python email_simulator.py
```

## 🧱 Classes

| Class   | Description                                      |
|---------|--------------------------------------------------|
| `Email` | Represents an email with sender, receiver, subject, body, and timestamp |
| `User`  | A user who can send emails and access their inbox |
| `Inbox` | Manages a list of emails with read/delete functionality |

## 💡 Example Usage

```python
tory = User('Tory')
ramy = User('Ramy')

tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
ramy.check_inbox()
ramy.read_email(1)
ramy.delete_email(1)
```

## 🛠️ Built With

- Python 3
- `datetime` module (standard library)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
