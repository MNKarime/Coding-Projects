'''
@author: Mohamad Nachat Karime
@date: 10/01/2022
'''

def calculate_budget(amount: float) -> float:
    food_and_groceries = float(input("How much do you want to spend on food/groceries each week? "))
    if food_and_groceries * 4 >= amount:
        print("The amount you entered would exhaust/exceed your monthly budget")
        exit()
    transportation = float(input("How much will you need to spend on transportation costs each week? "))
    if transportation * 4 >= amount:
        print("The amount you entered would exhaust/exceed your monthly budget")
        exit()

    housing = float(input("Enter your housing costs per month (i.e. mortgage, rent, etc) "))
    if housing >= amount:
        print("The amount you entered would exhaust/exceed your monthly budget")
        exit()

    utilities = float(input("Enter the cost of utilities per month "))
    if utilities >= amount:
        print("The amount you entered would exhaust/exceed your monthly budget")
        exit()

    insurance = float(input("Enter the cost of insurance per month (health, car, housing) "))
    if insurance >= amount:
        print("The amount you entered would exhaust/exceed your monthly budget")
        exit()
    car_payments = float(input("Enter the cost of you car payments, if any, otherwise enter 0 "))
    if car_payments >= amount:
        print("The amount you entered would exhaust/exceed your monthly budget")
        exit()

    
    amount_left = amount - ((food_and_groceries) * 4) - ((transportation) * 4) - housing  - utilities - insurance - car_payments
    
    if amount_left < 0:
        print("You do not have enough money to accommodate your expenses")
        exit()
    elif amount_left == 0:
        print("The amount you will be spending on food, groceries, and transportation is too high")
        exit()
    elif amount_left > 0:
        print("You will have $" + str(amount_left) + " left after taking care of your expenses")
    
    investments = amount_left * 0.35
    savings = amount_left * 0.4
    luxury = amount_left * 0.25
    
    print("Lets divide the amount you have left, $" + str(investments) + " will go into investments $" 
          + str(savings) + " will go into savings" + " and the remaining $" + str(luxury) + 
          " can be used for entertainment, shopping")
    
    user_input = str(input("Do you want to adjust any of your monthly costs? (Enter 'y' or 'n') "))
    if user_input == "y":
        user_input2 = str(input("Which of your costs would you like to adjust? "))
    elif user_input == "n":
        exit()
    
    
calculate_budget(7500)

    

