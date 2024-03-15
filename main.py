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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_user_decision():
    return input("What would you like? (espresso/latte/cappuccino): ")


def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def paid_coins():
    coins = 0
    print("Please insert money.")
    coins += int(input("How many quarters ($0.25)? ")) * 0.25
    coins += int(input("How many dimes ($0.10)? ")) * 0.10
    coins += int(input("How many nickles ($0.05)? ")) * 0.05
    coins += int(input("How many pennies ($0.01)? ")) * 0.01
    return coins


def make_coffee(drink, payment):
    cost = MENU[drink]["cost"]
    if payment < cost:
        print("Sorry, you inserted not enough money. Money refunded.")
    change = round(payment - cost, 2)
    if change > 0:
        print(f"You inserted too much money. Your change is {change}.")
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    is_on = True
    while is_on:
        decision = get_user_decision()
        if decision == "off":
            is_on = False
        elif decision == "report":
            for item, value in resources.items():
                print(f"{item}: {value}")
        if decision in MENU:
            if check_resources(decision):
                payment = paid_coins()
                make_coffee(decision, payment)


coffee_machine()
