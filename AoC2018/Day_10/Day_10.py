import re
import subprocess as sp
import matplotlib.pyplot as plt

R_pos = r'position=<(\s)*(-?\d*),(\s)*(-?\d*)>.*'
R_vel = r'.*velocity=<(\s)*(-?\d*),(\s)*(-?\d*)>'

class Point:
    def __init__(self, string):
        pos = re.match(R_pos, string)
        vel = re.match(R_vel, string)

        self.position = (int(pos.group(2)), int(pos.group(4)))
        self.velocity = (int(vel.group(2)), int(vel.group(4)))

    def tick(self, times=1):
        if times < 0:
            for _ in range(abs(times)):
                self.position = (self.position[0] - self.velocity[0], 
                                 self.position[1] - self.velocity[1])
        else:
            for _ in range(times):
                self.position = (self.position[0] + self.velocity[0], 
                                 self.position[1] + self.velocity[1])

    def __str__(self):
        return '(P:{pos}, V:{vel})'.format(pos=self.position, vel=self.velocity)

    def __repr__(self):
        return self.__str__()

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

def show_points(points):
    plt.scatter([p.x for p in points],
                [-p.y for p in points],
                marker='o')
    plt.show()

def ysize(points):
    return max(p.y for p in points) - min(p.y for p in points)

def xsize(points):
    return max(p.x for p in points) - min(p.x for p in points)

def find_min(points):
    prev_size = xsize(points) * ysize(points)
    t=0
    while True:
        t += 1
        for p in points:
            p.tick()

        cur_size = xsize(points) * ysize(points)

        if cur_size > prev_size:
            break

        prev_size = cur_size

    return t - 1

def part_1(points):
    steps = find_min(points)
    print(steps)
    for p in points:
        p.tick(-1)

    show_points(points)


ex = ['position=< 9,  1> velocity=< 0,  2>', 
      'position=< 7,  0> velocity=<-1,  0>', 
      'position=< 3, -2> velocity=<-1,  1>', 
      'position=< 6, 10> velocity=<-2, -1>', 
      'position=< 2, -4> velocity=< 2,  2>', 
      'position=<-6, 10> velocity=< 2, -2>', 
      'position=< 1,  8> velocity=< 1, -1>', 
      'position=< 1,  7> velocity=< 1,  0>', 
      'position=<-3, 11> velocity=< 1, -2>', 
      'position=< 7,  6> velocity=<-1, -1>', 
      'position=<-2,  3> velocity=< 1,  0>', 
      'position=<-4,  3> velocity=< 2,  0>', 
      'position=<10, -3> velocity=<-1,  1>', 
      'position=< 5, 11> velocity=< 1, -2>', 
      'position=< 4,  7> velocity=< 0, -1>', 
      'position=< 8, -2> velocity=< 0,  1>', 
      'position=<15,  0> velocity=<-2,  0>', 
      'position=< 1,  6> velocity=< 1,  0>', 
      'position=< 8,  9> velocity=< 0, -1>', 
      'position=< 3,  3> velocity=<-1,  1>', 
      'position=< 0,  5> velocity=< 0, -1>', 
      'position=<-2,  2> velocity=< 2,  0>', 
      'position=< 5, -2> velocity=< 1,  2>', 
      'position=< 1,  4> velocity=< 2,  1>', 
      'position=<-2,  7> velocity=< 2, -2>', 
      'position=< 3,  6> velocity=<-1, -1>', 
      'position=< 5,  0> velocity=< 1,  0>', 
      'position=<-6,  0> velocity=< 2,  0>', 
      'position=< 5,  9> velocity=< 1, -2>', 
      'position=<14,  7> velocity=<-2,  0>', 
      'position=<-3,  6> velocity=< 2, -1>', 
]


part_1([Point(L) for L in ex])
with open('input.txt') as f:
    points = [Point(L) for L in f]

part_1(points)

