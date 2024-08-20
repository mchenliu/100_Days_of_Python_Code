#treasure island

print('Welcome to Treasure Island. Your missions is to find the treasure.')

while True:
    input1 = input('You see 2 roads. Turn left or right?')
    if input1 == 'left':
        input2 = input('You see a lake. Swim or wait for a boat?')
        if input2 == 'wait':
            input3 = input('You see 3 doors. Which one would you pick? Blue, yellow or red?')
            if input3 == 'Blue':
                print('You are eaten by beasts. Game Over.')
                break
            elif input3 =='Red':
                print('You are burnt by fired. Game Over.')
                break
            elif input3 == 'Yellow':
                print('You win!')
                break
            else:
                print('Game Over.')
                break
        else:
            print('You were attacked by trout. Game Over.')
            break

    else:
        print('You fell into a hole. Game Over.')
        break
