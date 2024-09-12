# Solution for Supermarket
queue = []  # Create an empty list to act as the queue

while True:
    command = input()  # Read the command or customer name
    if command == 'End':  # If command is "End", stop and print how many people are left
        print(f"{len(queue)} people remaining.")
        break
    elif command == 'Paid':  # If command is "Paid", print and empty the queue
        for customer in queue:
            print(customer)
        queue.clear()  # Empty the queue
    else:
        queue.append(command)  # Add the customer's name to the queue
