from Secret_Auction_Program_Art import logo
print(logo)

print('Welcome to the secret auction program.')

bid_dic = {}
largest_bid = None

auction_over = False
while not auction_over:
    name = input('What is your name: ')
    bid = input('What is your bid: $')
    bid_dic[name] = bid
    
    bid = int(bid)
    if largest_bid is None or bid > largest_bid:
        largest_bid = bid
        
   
    other_bidders = input("Are there any other bidders? Enter 'yes' or 'no'\n").lower()
    print('\n'*100)
    if other_bidders == 'no':
        auction_over = True
#find the winning bidder
largest_bid = str(largest_bid)        
key_list = list(bid_dic.keys())
value_list = list(bid_dic.values())
position = value_list.index(largest_bid)
winning_bidder = key_list[position]
print(f'The winner is {winning_bidder} with the highest bid of ${largest_bid}.')
        
