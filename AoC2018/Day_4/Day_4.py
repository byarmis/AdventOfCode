import re
from collections import defaultdict
from datetime import datetime, timedelta

D = '%Y-%m-%d %H:%M'
R = r'\[(.*)\] (.*)'
R_text = r'Guard #(\d*) .*'

start = None
end = None

guards = dict()

class Guard:
    def __init__(self, s):
        ID = re.match(R_text, text)
        self.ID = int(ID.group(1))

        self.sleep = []
        self.awake = []
        self.begin = []

    def add(self, d, text):
        if 'falls asleep' in text :
            self.sleep.append( datetime.strptime(d, D))
        elif 'wakes up' in text:
            self.awake.append(  datetime.strptime(d, D))
        elif 'begins' in text:
            self.begin.append(datetime.strptime(d, D))

    def __hash__(self):
        return self.ID

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return 'Guard {}: Asleep {}, Awake {}, Beginning {}'.format(
                self.ID,
                ', '.join(str(s) for s in self.sleep), 
                ', '.join(str(s) for s in self.awake),
                ', '.join(str(s) for s in self.begin))

    def __repr__(self):
        return self.__str__()

    def combine_times(self):
        a = [('awake', t) for t in self.awake]
        s = [('sleep', t) for t in self.sleep]
        b = [('begin', t) for t in self.begin]

        times = []
        prev = None

        for t in sorted(a+s+b, key=lambda x: x[1]):
            if prev is None:
                prev = t[0]
                times.append((prev, t[1]))

                continue

            if prev != t[0]:
                prev = t[0]
                times.append((prev, t[1]))

        sleep_times=[]
        for t in zip(times, times[1:]):
            if t[0][0]=='sleep':
                sleep_times.append((t[0][1], t[1][1]))
            
        self.sleep_times = [range(t[0].minute, t[1].minute) for t in sleep_times]

    def total_asleep(self):
        return sum(len(t) for t in self.sleep_times)

with open('input_sorted.txt') as f:
    guard = None
    for line in f:
        line_split = re.match(R, line)

        date = line_split.group(1)
        text = line_split.group(2)

        if '#' in text:
            guard = Guard(text)

            if guard not in guards:
                guards[guard] = guard

        if guard is None:
            continue

        guards[guard].add(date, text)

_ = [g.combine_times() for g in guards]

sleepy_guard = max(guards.keys(), key=lambda x: x.total_asleep())

cnt = defaultdict(int)
for r in sleepy_guard.sleep_times:
    for t in r:
        cnt[t] +=1

m = 0
for k, v in cnt.items():
    if v > m:
        m = v
        cmax = k,v

print(sleepy_guard.ID * cmax[0])

# Holy crap, it worked on the first try?!

cnt = dict()
for guard in guards:
    for st in guard.sleep_times:
        for t in st:
            if t not in cnt:
                cnt[t] = {guard.ID:0}

            if guard.ID not in cnt[t]:
                cnt[t].update({guard.ID:0})

            cnt[t][guard.ID] += 1

max_cnt = 0
for minute in cnt:
    if max(cnt[minute].values()) > max_cnt:
        max_cnt = max(cnt[minute].values())
        max_minute = minute
        for k , v in cnt[minute].items():
            if v == max_cnt:
                max_grd = k

print(max_grd * max_minute)

