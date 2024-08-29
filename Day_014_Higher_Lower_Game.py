import random
from Day_014_Higher_Lower_Game_Art import logo, vs
from Day_014_Higher_Lower_Game_Data import data

score = 0
def pick_one():
    pick_one = random.choice(data)
    return pick_one.get('name'),pick_one.get('description'),pick_one.get('follower_count'),pick_one.get('country')
def answer_incorrect():
    global score
    print('\n'*50)
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.") 
def answer_correct():
    global score
    score += 1
        
    
def game():
    nameA, descriptionA, follower_countA, countryA = pick_one()
    nameB, descriptionB, follower_countB, countryB = pick_one()
    print(logo)
    print(f'Compare A: {nameA}, a {descriptionA}, from {countryA}')
    print(vs)
    print(f'Against B: {nameB}, a {descriptionB}, from {countryB}')
    if follower_countA > follower_countB:
        correct_answer = 'A'
    else:
        correct_answer = 'B'
        
    game_over = False
    while not game_over:
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_answer == correct_answer:
            answer_correct()
            print('\n'*50)
            print(logo)
            nameA = nameB
            descriptionA = descriptionB
            countryA = countryB
            
            print(f"You're right! Current score: {score}.")
            print(f'Compare A: {nameA}, a {descriptionA}, from {countryA}')
            pick_one()
            nameB, descriptionB, follower_countB, countryB = pick_one()
            print(vs)
            print(f'Against B: {nameB}, a {descriptionB}, from {countryB}')
            
            continue
        else:
            answer_incorrect()
            game_over = True
game()           








