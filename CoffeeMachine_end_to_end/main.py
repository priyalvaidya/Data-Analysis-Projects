from c_data import MENU, resources
from db import connect_to_mysql, insert_data


def check_res_sufficient(drink_choice):
    if (MENU[drink_choice]["ingredients"]["water"] <= resources["water"]):
        if (MENU[drink_choice]["ingredients"]["milk"] <= resources["milk"]):
            if (MENU[drink_choice]["ingredients"]["coffee"] <= resources["coffee"]):
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough milk.")
            return False
    else:
        print("Sorry there is not enough water.")
        return False

def process_coins(q, d, n, p):
    return float((q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01))

def check_amt_sufficient(amount_received, drink_choice):
    if (amount_received >= MENU[drink_choice]["cost"]):
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def calc_change(amount_received, drink_choice):
    return amount_received - MENU[drink_choice]["cost"]

def make_coffee(drink_choice, amount_received):
    print(f"Here is {round(calc_change(amount_received, drink_choice), 2)}$ in change.")
    print(f"Here it is your {drink_choice}. Enjoy!")

def changes_res(drink_choice, amount_received):
    resources["water"] = resources["water"] - MENU[drink_choice]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[drink_choice]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[drink_choice]["ingredients"]["coffee"]
    resources["money"] = resources["money"] + amount_received

if __name__ == "__main__":
    is_on = True
    while is_on:
        name = input("Enter your name: \n")
        order_date = input("Enter today's date: \n")
        action = input("What would you like to have? (Espresso/Latte/Cappuccino):\nPrices :\nEspresso - 1.5$\nLatte - 2.5$\nCappuccino -3$\n").lower()
        if action == "off":
            is_on = False
        elif action == "report":
            print(f"Resources available : {resources}")
        else:
            drink_choice = action
            amount = MENU[drink_choice]["cost"]

            if check_res_sufficient(drink_choice):
                print("Please insert coins.")
                quarter = int(input("How many quarters?:"))
                dime = int(input("How many dimes?:"))
                nickel = int(input("How many nickels?:"))
                penny = int(input("How many pennies?:"))

                amount_received = process_coins(quarter, dime, nickel, penny)

                if check_amt_sufficient(amount_received, drink_choice):
                    make_coffee(drink_choice, amount_received)
                    changes_res(drink_choice, amount_received)
                    conn = connect_to_mysql()
                    if conn:
                        insert_data(conn, order_date, name, drink_choice, amount)
                        conn.close()
