with open('input.txt') as f:
    expenses = [int(i) for i in f.readlines() if i.strip()]

expenses.sort()

def get_sum(i, j):
    return expenses[i] + expenses[j] 


def find_pair(goal):
    i = 0
    j = len(expenses) - 1

    while get_sum(i, j) != goal:
        if i == j:
            raise ValueError
        elif get_sum(i, j) < goal:
            i += 1
        elif get_sum(i, j) > goal:
            j -= 1

    return expenses[i]*expenses[j]

print("Part 1: ", find_pair(2020))

for e in expenses:
    try:
        f = find_pair(2020-e)
        print("Part 2: ", f*e)
        break

    except ValueError:
        continue

