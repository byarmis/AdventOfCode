import re

class Nanobot:
    def __init__(self, str_in):
        self.position = tuple(map(int, re.search(r'.*\<((-)?\d*,(-)?\d*,(-)?\d*)\>.*', str_in).group(1).split(',')))
        self.radius = int(re.search(r'.*r=(\d*)', str_in).group(1))

nanobots = []
with open('input.txt') as f:
    for line in f:
        nanobots.append(Nanobot(line))

max_bot = max(nanobots, key=lambda x: x.radius)

cnt = 0
for bot in nanobots:
    if (abs(bot.position[0] - max_bot.position[0]) + abs(bot.position[1] - max_bot.position[1]) + abs(bot.position[2] - max_bot.position[2])) <= max_bot.radius:
        cnt +=1

print(cnt)

# xmin = min(nanobots, key=lambda x: x.position[0]).position[0]
# ymin = min(nanobots, key=lambda x: x.position[1]).position[1]
# zmin = min(nanobots, key=lambda x: x.position[2]).position[2]
# 
# xmax = max(nanobots, key=lambda x: x.position[0]).position[0]
# ymax = max(nanobots, key=lambda x: x.position[1]).position[1]
# zmax = max(nanobots, key=lambda x: x.position[2]).position[2]
# 
# def get_count(nanobots, point):
#     cnt = 0
#     for bot in nanobots:
#         if (abs(bot.position[0] - point[0]) + abs(bot.position[1] - point[1]) + abs(bot.position[2] - point[2])) <= bot.radius:
#             cnt += 1
# 
#     return cnt
#
# dists = dict()
# for x in range(xmin-max_bot.radius, xmax+max_bot.radius):
#     for y in range(ymin, ymax+max_bot.radius):
#         for z in range(zmin-max_bot.radius, zmax+max_bot.radius):
#             dists[x,y,z] = get_count(nanobots, (x,y,z))
# 
# print('finding min dist')
# min_dist = (9999999999, 9999999999, 9999999999)
# min_cnt = 9999999999
# for k in dists:
#     if dists[k] < min_cnt and sum(k) < sum(min_dist):
#         min_dist = k
# 
# print(min_dist)
            
