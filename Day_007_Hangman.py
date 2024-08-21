# To do 1: randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it
import random
from hangman_art import stages, logo
from hangman_word_lst import word_list
print(logo)

chosen_word = random.choice(word_list)


#To do 2: ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
#To do 3: chek if the letter the user guessed is one of the letters in the chosen_word. Print 'Right' if it is. 'Wrong' is its not.
#To do 4: create an empty string called 'Placeholder'.For each letter in the chosen_word, add a _ to placeholder.
#To do 5: create a 'display' that puts the guess letter in the right place.
#To do 6: loop through each letter in the chosen_word. If the letter at that position matches guess then reveal that letter in the display at that position.
#To do 7: print display and you should see the guessed letter in the correct position.But every letter that is not a match is represented with a '_'

#To do 8: use a while loop to let the user guess again.
#To do 9: change the for loop so that you keep the previous correct guess

game_over = False
lst = []
lives = 6
while not game_over:
    print('****************************<???>/6 LIVES LEFT****************************')
    guess = input('Please guess a letter:').lower()
    
    if guess in lst:
        print(f"You've already guessed {guess}")
    
    word =''
    
    for i in chosen_word:
        if i == guess:
            word = word + i
            lst.append(i)
        elif i in lst:
            word = word + i        
        else:
            word = word + '_'
    print('Word to guess:',word)
    if guess not in chosen_word:
        lives = lives -1
        print('Your guess is not in the word. You have', lives, 'lives left.')
        
        if lives == 0:
            game_over = True
            print('Game over. You lose.')
            
            print(f'***********************IT WAS {chosen_word}! YOU LOSE**********************')
    
    print(word)
    
    
    if '_' not in word:
        game_over = True
        print('****************************YOU WIN****************************')
    print(stages[lives])

    
#To do 10: create a variable called lives to keep track of the number of lives left. Set lives to euqal to 6.
#To do 11: If guess is not a letter in the chosen_word, then reduce lives by 1. If lives goes fown to 0 then the game should end and it should print 'You lose'
#To do 12: Print the ASCII art from the list stages that corresponds to the current numbr of lives the use has remaining




        
        
    
