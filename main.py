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

decision = input("What would you like? (espresso/latte/cappuccino):")


def user_decision():
    if decision == "espresso":
        return "espresso"
    if decision == "latte":
        return "latte"
    if decision == "cappuccino":
        return "cappuccino"
    if decision == "report":
        for resource, value in resources.items():
            print(f"{resource}: {value}")


def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            return False
    return True


print(f"Your bill is {MENU[user_decision()]['cost']}.")


def paying(drink):
    coins, cost = 0, MENU[drink]["cost"]
    coins += int(input("How many quarters ($0.25)? ")) * 0.25
    coins += int(input("How many dimes ($0.10)? ")) * 0.10
    coins += int(input("How many nickles ($0.05)? ")) * 0.05
    coins += int(input("How many pennies ($0.01)? ")) * 0.01
    if coins < cost:
        print("Sorry, it is not enough money. Money refunded.")
    elif coins > cost:
        print(f"You inserted too much money. Your change is {round(coins - cost, 2)}")
    return coins


user_decision()
check_resources(user_decision())
paying(user_decision())
