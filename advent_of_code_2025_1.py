with open('advent_of_code_2025_1_input', 'r') as file:
# with open('tmp', 'r') as file:
    contents = file.readlines()

pwd = 0
total = 50
for line in contents:
    code = line.strip()
    direction, magnitude = code[0], int(code[1:])
    for i in range(magnitude):
        if direction == 'L':
            total -= 1
        else:
            total += 1
        total %= 100
        if total == 0:
            pwd += 1
print(pwd)