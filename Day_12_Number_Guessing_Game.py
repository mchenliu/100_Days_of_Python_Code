
#randomly generate a number
import random
CORRECT_ANSWER = random.randint(1,100)

from Day_12_Number_Guessing_Game_Art import logo

#welcoming message
print(logo)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")

#player picking game level
level = input(("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
if level == 'easy':
    print('You have 10 attempts remaining to guess the number.')
    lives = 10
    
else:
    print('You have 5 attempts remaining to guess the number.')
    lives = 5
    




#function to reduce live

def reduce_a_life(live):
    return live -1




#game without loop
game_over = False
while not game_over:
    guess = int(input(('Make a guess: ')))
    if guess > CORRECT_ANSWER:
        print('Too high.')
        lives = reduce_a_life(lives)
        if lives == 0:
            game_over = True
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")
            print(f'You have {lives} attempts remaining to guess the number.')
        
        
    elif guess < CORRECT_ANSWER:
        print('Too low.')
        lives = reduce_a_life(lives)
        if lives == 0:
            game_over = True
            print("You've run out of guesses, you lose.")
        else:
            print('Guess again.')
            print(f'You have {lives} attempts remaining to guess the number.')
        
        
        
    else:
        game_over = True
        print(f'You got it! The answer was {CORRECT_ANSWER}')


        

