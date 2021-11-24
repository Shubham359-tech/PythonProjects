# Prompt user by asking “What would you like? (espresso/latte/cappuccino)


# Setting up while loop
off = False

profit = 0
water = 100
Milk = 50
Coffee = 76
Money = 0
while not off:

    def calCoins():
        print("Please Insert Coins For your Drink!!!")
        print(f"quarters, dimes, nickles, pennies")
        qn = float(input("number of Quarters"))
        dn = float(input("number of Dimes"))
        nn = float(input("number of nickels"))
        pn = float(input("number of pennies"))
        calculateCoins = (0.25 * qn) + (0.10 * dn) + (0.05 * nn) + (0.01 * pn)

        return calculateCoins


    def process():

        global water, Milk, Coffee, profit,Money
        userInput2 = int(input("If you want to see report please enter 1 : "))

        if userInput2 == 1:
            print(f" Water : {water} ml\n Milk : {Milk} ml\n Coffee : {Coffee} ml  ")

        userInput1 = input("What would you like?(espresso/latte/cappuccino) \n")

        if userInput1 == "espresso" and water > 9 and Milk > 5 and Coffee > 3:
            Money = 1.5
            print(f"espresso will cost {Money}")
            water -= 9
            Milk -= 5
            Coffee -= 3
            profit += Money
            Cal = calCoins()
            print(Cal)
            if Cal > 1.5:
                print(f"Your Change Is Here : {Cal - Money}")
            if Cal < 1.5:
                print("Sorry Not Enough Money")

            print(f"Profit = {profit}")
            print(f" Water : {water} ml\n Milk : {Milk} ml\n Coffee : {Coffee} ml  ")

        elif userInput1 == "latte" and water > 9 and Milk > 5 and Coffee > 3:
            Money = 2.5
            print(f"latte will cost {Money}")
            water -= 9
            Milk -= 5
            Coffee -= 3
            profit = 0
            Cal = calCoins()
            print(Cal)
            if Cal > 2.5:
                print(f"Your Change Is Here : {Cal - Money}")
            if Cal < 2.5:
                print("Sorry Not Enough Money")
            profit += Money
            print(f"Profit = {profit}")

        elif userInput1 == "cappuccino" and water > 9 and Milk > 5 and Coffee > 3:
            Money = 3
            print(f"cappuccino will cost {Money}")
            water -= 9
            Milk -= 5
            Coffee -= 3
            Cal = calCoins()
            print(Cal)
            if Cal > 3:
                print(f"Your Change Is Here : {Cal - Money}")
            if Cal < 3:
                print("Sorry Not Enough Money")
            profit += Money
            print(f"Profit = {profit}")

        else:
            print("There is not enough stuff available sorry for inconvenience")
    process()
    if input("Do you want to buy again 'Yes' or 'NO' ").lower() == "yes":
        process()
    else:
        off = True
