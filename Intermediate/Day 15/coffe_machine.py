from menu import MENU, resources


def print_report():
    print(f"""
Water: {machine_resources["water"]}ml
Milk: {machine_resources["milk"]}ml
Coffee: {machine_resources["coffee"]}g
Money: ${machine_resources['money']}
""")

def check_resources_sufficient(userinput):
    drink = MENU[userinput]
    for item in drink["ingredients"]:
        if (drink["ingredients"][item] > machine_resources[item]):
            print(f"Sorry there is not enough {item}.")
            return
        
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    machine_resources["money"] = process_coins(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
    if drink["cost"] > machine_resources["money"]:
        print("Sorry that's not enough money. Money refunded.")
        machine_resources["money"] = 0
        return

    make_coffee(drink)
    print(f"Here is ${machine_resources["money"]} in change.")
    print(f"Here is your {userinput} ☕. Enjoy!.")

def process_coins(quarters, dimes, nickles, pennies):
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def make_coffee(drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    machine_resources["money"] -= drink["cost"]
    return

machine_resources = resources
machine_resources["money"] = 0.0
machine_on = True
while machine_on:
    machine_resources["money"] = 0.0
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        break
    elif user_input == "report":
        print_report()
    else:
        check_resources_sufficient(user_input)