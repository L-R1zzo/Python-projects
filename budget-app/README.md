# Budget App 💰

A simple Python app to track income and expenses across multiple categories, with a visual spending chart.

---

## What it does

- Create budget categories (Food, Clothing, etc.)
- Deposit and withdraw amounts with descriptions
- Transfer funds between categories
- Check the balance at any time
- Print a formatted ledger for each category
- Generate a bar chart showing spending by category

---

## Getting started

No external libraries needed — just Python 3.

```bash
git clone https://github.com/your-username/budget-app.git
cd budget-app
python main.py
```

---

## Usage

```python
from budget import Category, create_spend_chart

# Create categories
food = Category('Food')
clothing = Category('Clothing')

# Deposit
food.deposit(1000, 'initial deposit')

# Withdraw
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant')

# Transfer between categories
food.transfer(50, clothing)

# Check balance
print(food.get_balance())  # 923.96

# Print ledger
print(food)

# Spending chart
print(create_spend_chart([food, clothing]))
```

---

## Example output

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant              -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o     
  0| o  o     
    ----------
     F  C     
     o  l     
     o  o     
     d  t     
        h     
        i     
        n     
        g     
```

---

## Methods

| Metodo | Descrizione |
|--------|-------------|
| `deposit(amount, description)` | Aggiunge un importo al ledger |
| `withdraw(amount, description)` | Sottrae un importo (se il saldo è sufficiente) |
| `transfer(amount, category)` | Trasferisce fondi a un'altra categoria |
| `get_balance()` | Restituisce il saldo attuale |
| `check_funds(amount)` | Restituisce `True` se il saldo copre l'importo |

---

## Project structure

```
budget-app/
├── budget.py      # Category class and create_spend_chart
├── main.py        # Example usage
└── README.md
```

---

## Built with

- Python 3
