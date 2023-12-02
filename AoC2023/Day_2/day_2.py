with open('input.txt') as f:
    lines = f.readlines()

possible_games = 0
powers = 0 
for line in lines:
    game, draws = line.split(':')
    game_num = int(''.join(i for i in game if i.isdigit()))

    draws = draws.split(';')

    possible = True
    cubes = {'red':None, 'green':None, 'blue':None}
    for draw in draws:
        for num_color_pair in draw.split(','):
            num, color = num_color_pair.strip().split(' ')
            num = int(num)
            if (num > 12 and color == 'red') or (num > 13 and color == 'green') or (num > 14 and color == 'blue'):
                possible = False

            cubes[color] = max(cubes[color] or int(num), int(num))

    if possible:
        possible_games += game_num

    power = cubes['red'] * cubes['green'] * cubes['blue']
    powers+= power

print(possible_games)
print(powers)



