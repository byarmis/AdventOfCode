
times = [40, 82, 91, 66]
distances = [277, 1338, 1349, 1063]

m = 1
for t, d in zip(times, distances):
    res = 0
    for hold_down in range(t+1):
        speed = hold_down
        time_remaining = t - hold_down
        distance_traveled = speed * time_remaining
        if distance_traveled > d:
            res += 1
    m *= res

print('Part 1: ', m)

time = 40829166
distance = 277133813491063

res = 0
for hold_down in range(time+1):
    speed = hold_down
    time_remaining = time - hold_down
    distance_traveled = speed * time_remaining
    if distance_traveled > distance:
        res += 1

print('Part 2: ', res)
