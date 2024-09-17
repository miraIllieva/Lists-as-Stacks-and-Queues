# 1. Reverse Numbers
# Write a program that reads a string with N integers from the console, 
# separated by a single space, and reverses them using a stack.
# Print the reversed integers on one line, separated by a single space.

# Function to reverse numbers using a stack
def reverse_numbers():
    # Read the input string and split it into a list of integers
    numbers = input("Enter numbers separated by spaces: ").split()

    # Create an empty stack (list) to store the numbers
    stack = []

    # Push all numbers onto the stack
    for num in numbers:
        stack.append(num)

    # Pop numbers from the stack to reverse their order
    reversed_numbers = []
    while stack:
        reversed_numbers.append(stack.pop())

    # Print the reversed numbers, joined by a space
    print(" ".join(reversed_numbers))

# Call the function to execute
reverse_numbers()
