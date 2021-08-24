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

#n1= int(input("Enter a number 1: "))
#operation= str(input("Enter the operation: "))
#n2 =int(input("Enter a number 2: "))

# Method 1
"""
if operation == '+':
    print(add(n1, n2))
elif operation == '-':
    print(sub(n1, n2))
elif operation == '*':
    print(mult(n1, n2))
elif operation == '/':
    print(div(n1, n2))
   """
#Method 2

operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
}

for symbol in operations:
    print(symbol)

n1=int(input("Enter number 1: "))
operation_symbol = input("Pick an operation from the line above: ")
n2=int(input("Enter number 2: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(n1, n2)
print(f'{n1} {operation_symbol} {n2} = {answer}')
