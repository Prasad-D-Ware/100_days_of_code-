logo = """/~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_enough(order_ingredients):
    """Returns True when order can be made ,False if ingredients are not enough"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_coins():
    """Returns the total calculated from the coins inserted"""

    print("Please insert the coins: ")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickel? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    """ "Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕️!")


is_machine_on = True

while is_machine_on:
    # prompt user for order
    print(logo)
    choice = input("What would you like to have ? (espresso/latte/cappuccino) : ")
    # turn of the machine if needed
    if choice == "off":
        is_machine_on = False
    # print report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    # check resources sufficient
    else:
        order = MENU[choice]
        print(order)
        if is_resources_enough(order["ingredients"]):
            # process coins
            payment = process_coins()
            # check transaction successfull
            if is_transaction_successful(payment, order["cost"]):
                # make coffee
                make_coffee(choice, order["ingredients"])
