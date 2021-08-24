# Calculator

# Add
def add(n1,n2):
    return n1+n2

# Subtract
def sub(n1, n2):
    return n1-n2

#multiply
def mult(n1, n2):
    return n1*n2

# Divide
def div(n1, n2):
    return n1/n2

operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
}

from art_calculator import logo
def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    for symbol in operations:
        print(symbol)
    ask = True
    while ask:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        ask = str(input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start new "
                        f"calculation or enter 'q' to quit:"))

        if ask == 'y':
            num1=answer
        elif ask =='n':
            calculator()
        elif ask=='q':
            ask = False

calculator()


