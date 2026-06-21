class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
    
    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
            })
        
        self.get_balance()
    
    def get_balance(self):
        self.balance = 0
        for dicts in self.ledger:
            self.balance += dicts["amount"]
        return self.balance    
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({    
                "amount": -amount,
                "description": description
                })
            self.get_balance()
            return True
        else:
            return False

    def transfer(self, amount, instance):
        if self.withdraw(amount, f"Transfer to {instance.name}"):
            instance.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False    

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        header = "*"*round(((30 - len(self.name))/2)) + self.name + "*"*round(((30 - len(self.name))/2)) + "\n"

        body = ""
        for dicts in self.ledger:
            description = dicts["description"]
            amount = dicts["amount"]
            amount = f"{amount:.2f}"
            if len(description) > 24:
                body += f"{description[:23]} {amount}\n"
            else: 
                body += description + " "*round((30 - len(description) - len(amount))) + amount + "\n"

        end = f"Total: {self.balance}"

        return header + body + end

def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total = sum(-d["amount"] for d in cat.ledger if d["amount"] < 0)
        spent.append(total)
    
    total_spent = sum(spent)
    percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    chart = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        row = f"{i:3}| "
        for p in percentages:
            row += "o  " if p >= i else "   "
        chart += row + "\n"
    
    chart += "    -" + "---" * len(categories) + "\n"
    
    max_len = max(len(cat.name) for cat in categories)
    
    for i in range(max_len):
        row = "     "
        for cat in categories:
            if i < len(cat.name):
                row += cat.name[i] + "  "
            else:
                row += "   "
        if i < max_len - 1:
            chart += row + "\n"
        else:
            chart += row
    
    return chart
        


