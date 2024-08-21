#Our Blackjack Game House Rules
#The deck is unlimited in size.
##The cards in the list have equal probability of being drawn.
#Cards are not removed from the deck as they are drawn.
#The computer is the dealer.
#if  sum < 17. The dealer has to draw a card
#c = computer
#u = user

#seperate player and dealer
#2 parties -
#player(p) & dealer(d)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#function for drawing a card

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
