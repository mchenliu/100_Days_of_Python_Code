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
    

            




# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message.
# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.



        
 

    







