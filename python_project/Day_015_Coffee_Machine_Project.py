from Day_015_Coffee_Machine_Project_Data import MENU, resources
#add milk to espresso menu
MENU["espresso"]["ingredients"]['milk']=0
#add money to resources dictionary
resources['Money']=0
#assign global report
report = resources
money = 0

machine_off = False
while not machine_off:
    user_choice = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if user_choice == 'off':
        machine_off = True
        
    elif user_choice == 'report':
        for k, v in report.items():
            if k == 'water':
                print(f'Water: {v}ml')
            elif k == 'milk':
                print(f'Milk: {v}ml')
            elif k == 'coffee':
                print(f'Coffee: {v}g')
            else:
                print(f'Money: ${v}')
                
        
    else: #check resources needed
        resources_needed = MENU[user_choice]['ingredients']
        estimation = {key: report[key] - resources_needed[key] for key in set(resources_needed) & set(report)}
        drink_cost = MENU[user_choice]['cost'] 
        estimation['Money'] = money  
                
        for k, v in estimation.items():
            if k == 'coffee' and v <= 0:
                print('Sorry there is not enough coffee.')
                break                                      
            if k == 'water' and v <= 0:
                print('Sorry there is not enough water.') 
                break
            if k == 'milk' and v <= 0:
                print('Sorry there is not enough milk.')
                break 
            
            #proceed to payment check                  
            else: 
                print('Please insert coins.')
                quarters = int(input('how many quarters?: '))*0.25
                dimes = int(input('how many dimes?: '))*0.1
                nickles = int(input('how many nickles?: '))*0.05
                pennies = int(input('how many pennies?: '))*0.01
                total = quarters + dimes + nickles + pennies

                if total < drink_cost:
                    print("Sorry that's not enough money. Money refunded.")
                    break
                
                else:
                    change = round(total - drink_cost,2)
                    money += MENU.get(user_choice).get("cost")
                    report = estimation
                    report['Money'] = money
                    print(f"Here is ${change} in change.")
                    print(f"Here's your {user_choice} ☕. Enjoy!")
                break
                    
    
        
    
        

   
    
    
    

