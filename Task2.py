input_string = input()
reverse_string = ""

for i in range(len(input_string) -1,-1,-1):
    reverse_string += input_string[i]

print(reverse_string)

