number = int(input())
students = {}

for _ in range(number):
    name, grade = input().split()
    grade = float(grade)

    if name in students:
        students[name].append(grade)

    else:
        students[name] = [grade]

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    grade_str = " ".join(str(g) for g in grades)
    print(f"{name} -> {grade_str} (avg: {avg:.2f})")
