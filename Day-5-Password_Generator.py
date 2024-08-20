#password generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print('Welcome to the Pypassword Generator!')
nr_letters = int(input('How many letters would you like in your password? \n'))
nr_symbols = int(input('How many symbols would you like? \n'))
nr_numbers = int(input('How many numbers would you like? \n'))

import random
input_letters = random.sample(letters,nr_letters)
input_symbols = random.sample(symbols, nr_symbols)
input_numbers = random.sample(numbers,nr_numbers)

new_lst = input_letters + input_symbols + input_numbers
random.shuffle(new_lst)
password = ''
for i in new_lst:
    password += (i)
print('Your password is', password)

