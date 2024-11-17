#rock paper scissors 
import random
user_input = input('What do you choose? Rock, Paper or Scissors?')
possible_actions = ['rock','paper','scissors']
computer_action = random.choice(possible_actions)
print('You chose', user_input, 'The compuer chose', computer_action)

      
if user_input == computer_action:
      print('It is a draw.')

elif user_input == 'paper':
      if computer_action == 'rock':
        print('You win!')
      else:
        print('You lose!')
elif user_input == 'scissors':
      if computer_action == 'paper':
        print('You win!')
      else:
        print('You lose!')
elif user_input == 'rock':
      if computer_action == 'scissors':
        print('You win!')
      else:
        print('You lose!')

        
##rock paper scissors version 2
#import random
#user_choice = input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors?')
#possible_choices = (0,1,2)
#computer_action = random.choice(possible_choices)
#
##print('You chose',user_choice,'And the computer chose',computer_action)
#
#if user_choice == computer_action:
#    print('It is a draw!')
#elif user_choice == 0:
#    if computer_choice == 2:
#        print('Rock smashes scissors. You win!')
#    else:
#        print('Paper covers rock. You lose!')
#elif user_choice == 1:
#    if computer_choice == 0:
#        print('Paper covers rock. You win!')
#    else:
#        print('Scissors cut paper. You lose!')
#elif user_choice == 2:
#    if computer_choice == 1:
#        print('Scissors cut paper. You win!')
#    else:
#        print('Rock smashes scissors. You lose!')
#    
