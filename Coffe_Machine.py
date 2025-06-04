menu = {
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
    "water": 1000,
    "milk": 500,
    "coffee": 250,
}


profit=0

def resource():
    print("Water:",resources["water"],"ml")
    print("Milk:",resources["milk"],"ml")
    print("Coffee:",resources["coffee"],"g")
    print(f"Money: ${profit}")

def check_deduct(drink_name):
    for item in menu[drink_name]["ingredients"]:
        if resources[item]<menu[drink_name]["ingredients"][item]:
            print(f"Sorry! we don't have enough {item} for placing your order")
            return False
    for item in menu[drink_name]["ingredients"]:
        resources[item]-=menu[drink_name]["ingredients"][item]
    return True

def coins():
    print("Please insert coins")
    quarters=int(input("How many quarters?"))*0.25
    dimes=int(input("How many dimes?"))*0.10
    nickles=int(input("How many nickles?"))*0.05
    pennies=int(input("How many pennies?"))*0.01
    global total
    total=quarters+dimes+nickles+pennies

def espresso():
    cost=menu["espresso"]["cost"]
    if total>=cost:
        remaining=round(total-cost,2)
        print(f"Here is ${remaining} in change.")
        print("Here is your espresso ☕️. Enjoy!")
        global profit
        profit+=cost
    else:
        print("Sorry that's not enough money. Money refunded.")


def latte():
    cost=menu["latte"]["cost"]
    if total>=cost:
        remaining=round(total-cost)
        print(f"Here is ${remaining} in change.")
        print("Here is your latte ☕️. Enjoy!")
        global profit
        profit+=cost

    else:
        print("Sorry that's not enough money. Money refunded.")

def cappuccino():
    cost=menu["cappuccino"]["cost"]
    if total>=cost:
        remaining=round(total-cost)
        print(f"Here is ${remaining} in change.")
        print("Here is your cappuccino ☕️. Enjoy!")
        global profit
        profit+=cost
    else:
        print("Sorry that's not enough money. Money refunded.")


always_continue=True
while always_continue:
    entry=input("What would you like? (espresso/latte/cappuccino): ")
    if entry=="report":
        resource()
    elif entry=="off":
        always_continue=False
    elif entry=="espresso":
        if check_deduct("espresso"):
            coins()
            espresso()
    elif entry=="latte":
        if check_deduct("latte"):
            coins()
            latte()
    elif entry=="cappuccino":
        if check_deduct("cappuccino"):
            coins()
            cappuccino()
    else:
        print("Invalid entry! Please try Again")


