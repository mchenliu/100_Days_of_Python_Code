# Introduction
:bug: This project records my on going Python learning journey following [Angela Yu's course](https://www.udemy.com/course/100-days-of-code)

:computer: Python codes? Check them out here: [python_project folder](/python_project/)

# The goal I wanted to achieve through my Python journey are:

1. :page_with_curl: Demonstrate my Python skills
2. :microscope: Land on a data analyst role

# Tools I Used
- **Python:** The backbone of this project, allow me to import packages and write codes.
- **PyCharm:** My go-to for storing and running Python scripts.
- **Windows Terminal:** Execute Python code.
- **Git & Github:** Platform for version control and sharing my Python codes. Helps with my project tracking.


# What I Learned

### :mag: The basics: 

**1. Variable and Data Types** ( :beers: Project Tip Calculator)
    
```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage of tip would you like to give?\n"))
ppl = int(input("How many people to split the bill?\n"))

totalbill = bill * (1+tip/100)
final= round(totalbill/ppl,2)

print(f"Each person should pay: ${final}")
``` 
**2. Control Flow and Logical Operators** ( :angel:Project Hangman)
```python
import random
from hangman_art import stages, logo
from hangman_word_lst import word_list
print(logo)

chosen_word = random.choice(word_list)

game_over = False
lst = []
lives = 6
while not game_over:
    print('****************************6 LIVES LEFT****************************')
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
```
**3. Randomisation, Loops and Lists** ( :jack_o_lantern:Project Caesar Cipher)
```python
from caesar_cipher_art import logo
print(logo)

def caesar (original_text, shift_amount, encode_or_decode):
    word = ''
    shift_amount %= len(alphabet)
    if encode_or_decode == 'decode':
        shift_amount = shift_amount *-1
    for i in text:
        if i not in alphabet:
            word +=i
        else:
            x = alphabet.index(i)
            num = x + shift_amount
            i = alphabet[num]
            word += i
    print(f'Here is the {direction}d result: {word}')
    
    
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game_over = False
while not game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text=text, shift_amount=shift,encode_or_decode=direction)
    
    restart = input("Do you want to try again? Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == 'no':
        game_over = True
        print('Goodbye.')
```
**4. Dictionary and Scopes** ( :mahjong:Project Blackjack)
```python
#Our Blackjack Game House Rules
#The deck is unlimited in size.
##The cards in the list have equal probability of being drawn.
#Cards are not removed from the deck as they are drawn.
#The computer is the dealer.
#if  sum < 17. The dealer has to draw a card

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_draw():
    new_card = random.sample(cards,1)
    return new_card
stop = False
while not stop:

starter = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

from Day_11_Blackjack_art import logo
import random
if starter =='y':
    print(logo)
    #player's first card draw

    player_cards = card_draw() + card_draw()
    p_sum = 0
    for i in player_cards:
        p_sum += i
    print(f'    Your cards: {player_cards}, current score: {p_sum}')

    #dealer section
    dealer_card_1 = card_draw()
    dealer_card_2 = card_draw()
    dealer_deck = dealer_card_1 + dealer_card_2
    print(f"    Dealer's first card: {dealer_card_1}")

    #check dealer sum
    dealer_pass = False
    while not dealer_pass:
        dealer_sum = 0
        for i in dealer_deck:
            dealer_sum +=i

        if dealer_sum < 17:
            dealer_deck += card_draw()
        else:
            dealer_pass = True
            
    #keep drawing or not
    #player section
    game_over = False
    while not game_over:
        q_to_ask = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if q_to_ask == 'y':
            player_cards = player_cards + card_draw()
            p_sum = 0
            for i in player_cards:
                p_sum += i
            print(f'    Your cards:{player_cards}, current score: {p_sum}')
            print(f"    Dealer's first card: {dealer_card_1}")
            if p_sum > 21:
                game_over = True
                print(f'    Your final hand: {player_cards}, final score: {p_sum}')
                print(f"    Dealer's final hand: {dealer_deck}, final score: {dealer_sum}")
        else:
            game_over = True
            print(f'    Your final hand: {player_cards}, final score: {p_sum}')
            print(f"    Dealer's final hand: {dealer_deck}, final score: {dealer_sum}")

    #result
    if p_sum > 21:
        print('You went over. You lose.')
        
    elif p_sum <21 and dealer_sum >21:
        print('Opponent went over. You win')

    elif p_sum == dealer_sum:
        print('Draw')

    elif p_sum < dealer_sum:
        print('You lose')

    else:
        print('You win')
```

### :bulb: Intermediate:

**1. Object Oriented Programming (OOP)** ( :clipboard:Project Quiz)

```python
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank =[]

for q in question_data:
    q_text = q["question"]
    q_answer = q["correct_answer"]
    new_question = Question(q_text,q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f'Your final score was: {quiz.score}/{len(quiz.question_list)}')    
```
**2. Graphical User Interface (GUI) ( :turtle:Project Turtle)**
```python
import turtle as t
import random
t= Turtle()
t.shape('turtle')
t.color('blue')
color = ['medium aquamarine','deep pink','dark magenta','light coral','orange','saddle brown','hot pink','dark green','medium blue']

#task 2 draw a dashed line
for i in range (40):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

#task 3 drawing different shapes with random color
def repeat(n):
  angle = 360/n
  for i in range(n):
    t.forward(50)
    t.right(angle)
for i in range(4,11):
  t.color(random.choice(color))
  repeat(i)
#Task 4 Random Walk with random speed, thickness and random color

directions = [0,90,180,270]
speed = range(0,11)
pensize = range(0,11)
def random_walk():
    t.setheading(random.choice(directions))
    t.speed(random.choice(speed))
    t.color(random.choice(color))
    t.pensize(random.choice(pensize))
    t.forward(10)
while True:
    random_walk()


#Task 5 random color with RGB colours
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
  
 t.color(random_color())
#Task 6 Make a Spirograph
for i in range(0,360,10):
    t.color(random_color())
    t.circle(100)
    t.setheading(i)
screen=Screen()
screen.exitonclick()
```

# Conclusions

This is an on-going project. 

### Closing Thoughts

Continous learning is a must to achieve goals in this area.