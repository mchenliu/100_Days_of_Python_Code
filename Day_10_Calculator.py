from Calculator_art import logo

def add (n1,n2):
    return n1 + n2
def subtract (n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide (n1,n2):
    return n1 / n2


operators = {
    '+': add, 
    '-': subtract, 
    '*' : multiply,
    '/': divide
}


def calculator():
    print(logo)
    stop = False
    n1 = float(input("What's the first number?: "))
        
    
    
    while not stop: 
        
        
        for i in operators:
            print(i)
        
        operations = input('Pick an operation: ')
        calc_function = operators[operations]
        
        n2 = float(input("What's the next number?: "))
        
        result = calc_function(n1,n2)

        print(f"{n1} {operations} {n2} = {result}")

        q_to_ask = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if q_to_ask == 'y':
            n1 = result
            
        else:
            stop = True
            print('\n'*20)
            calculator()

calculator()



