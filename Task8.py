numbers = input().split()
occurrences = {}

for num in numbers:
    num = float(num)
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

for num, count in occurrences.items():
    print(f"{num:.1f} - {count} times")
