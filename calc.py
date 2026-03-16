a = float(input("Enter the first number"))
b = float(input("enter the second number"))
print("choose operations: + for additon, - for subtraction, * for multiplication, / for division")
op = input("Enter operation")
if op == "+":
    result = a + b
elif op == "-":
    result = a - b 
elif op == "*":
    result = a * b  
elif op == "/":
    result = a / b 
else:
    result = "Invalid operation"
print("The result is:", result)

# This is a simple calculator program that performs basic arithmetic operations based on user input.