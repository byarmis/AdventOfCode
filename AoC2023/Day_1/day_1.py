
with open('input.txt') as f:
    lines = f.readlines()

sums = 0
for line in lines:
    val = ''
    for char in line:
        if char.isdigit():
            val += char
            break

    for char in line[::-1]:
        if char.isdigit():
            val += char
            break

    sums += int(val)

print(sums)

sums = 0

numbers = ['!', 'one' , 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in lines:
    numbers_in_line = {loc: val for loc, val in enumerate(line) if val.isdigit()}

    for number in numbers:
        if number in line:
            # First
            numbers_in_line[line.index(number)] = str(numbers.index(number))

        if number[::-1] in line[::-1]:
            numbers_in_line[len(line) - line[::-1].index(number[::-1])-len(number)] = str(numbers.index(number))


    first = min(numbers_in_line.keys())
    last = max(numbers_in_line.keys())
    val = numbers_in_line[first] + numbers_in_line[last]

    sums += int(val)
print(sums)

