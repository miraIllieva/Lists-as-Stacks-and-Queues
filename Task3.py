# Solution for Matching Parentheses
expression = input()  # Read the algebraic expression
stack = []  # To store the indices of opening parentheses

# Loop through the expression to find matching parentheses
for i in range(len(expression)):
    if expression[i] == '(':  # When you find an opening parenthesis
        stack.append(i)  # Add its index to the stack
    elif expression[i] == ')':  # When you find a closing parenthesis
        start_index = stack.pop()  # Get the last opening parenthesis index
        print(expression[start_index:i+1])  # Print the content inside the parentheses
