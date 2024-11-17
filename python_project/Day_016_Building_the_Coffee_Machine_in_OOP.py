from Day_016_Building_the_Coffee_Machine_in_OOP_Menu import Menu, MenuItem
from Day_016_Building_the_Coffee_Machine_in_OOP_Coffee_Maker import CoffeeMaker
from Day_016_Building_the_Coffee_Machine_in_OOP_Money_Machine import MoneyMachine


ben = Menu()
steven = CoffeeMaker()
andrew = MoneyMachine() 

machine_off = False

while not machine_off:
    user_choice = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if user_choice == 'report':
        steven.report()
        andrew.report()
    elif user_choice == 'off':
        quit()
    else:
        order = ben.find_drink(user_choice)
        check = steven.is_resource_sufficient(order)
        if check is True:
            take_money = andrew.make_payment(order.cost)
            if take_money is True:
                make_coffee = steven.make_coffee(order)
            else:
                take_money
        else:
            print(check)


