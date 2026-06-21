# example code

from budget import Category, create_spend_chart

food = Category('Food')
clothing = Category('Clothing')

food.deposit(1000, 'initial deposit')

food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant')

food.transfer(50, clothing)

print(food.get_balance())  

print(food)

print(create_spend_chart([food, clothing]))
