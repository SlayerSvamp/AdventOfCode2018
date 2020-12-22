from itertools import count
from base64 import _b85alphabet as timechar
from sys import setrecursionlimit
setrecursionlimit(10000)

depth = 6084
target = 14, 709

# ##### test #### #
# depth = 510     #
# target = 10, 10 #
# ############### #

tx, ty = target

margin = 10
regionSize = 2


class Tool:
    neither = 0
    torch = 1
    climbing_gear = 2


class Type:
    rocky = 0
    wet = 1
    narrow = 2


type_text = ['rocky', 'wet', 'narrow']
tool_text = ['neither', 'torch', 'climbing gear']
type_char = '.=|'
type_tools = [(1, 2), (0, 2), (0, 1)]

tool_switch = [3, 2, 1]


class Region:
    regions = {}

    @staticmethod
    def get(x, y):
        if x < 0 or y < 0:
            return None
        if (x, y) in Region.regions:
            return Region.regions[x, y]
        return Region(x, y)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        if y == ty and x == tx:
            self.index = 0
        elif y == 0:
            self.index = x * 16807
        elif x == 0:
            self.index = y * 48271
        else:
            self.index = Region.get(x-1, y).erosion
            self.index *= Region.get(x, y-1).erosion

        self.erosion = (self.index + depth) % 20183
        self.type = self.erosion % 3
        Region.regions[x, y] = self

    def char(self):
        if self.x == tx and self.y == ty:
            return 'T'
        if self.x == 0 and self.y == 0:
            return 'M'
        return type_char[self.type]


target_state = (tx, ty, Tool.torch)
target_state_switched = (tx, ty, Tool.climbing_gear)
visited = {
    (0, 0, Tool.torch): 0
}
directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def adjacent(x, y):
    for _x, _y in directions:
        yield Region.get(x + _x, y + _y)


for time in count():
    for (x, y, tool) in [state for state, passed in visited.items() if passed == time]:
        for region in adjacent(x, y):
            if not region:
                # or region.y > (ty + 300) or region.x > (tx + 500):
                continue
            if tool in type_tools[region.type]:
                state = (region.x, region.y, tool)
                if state not in visited or visited[state] > (time + 1):
                    visited[state] = time + 1
            else:
                state = (region.x, region.y, tool ^ tool_switch[region.type])
                if state not in visited or visited[state] > (time + 8):
                    visited[state] = time + 8
    if target_state_switched in visited and (target_state not in visited or visited[target_state] > visited[target_state_switched] + 7):
        print(visited[target_state_switched])
        if target_state in visited:
            print(visited[target_state])
        visited[target_state] = visited[target_state_switched] + 7
        print(visited[target_state])
    if target_state in visited and visited[target_state] >= time + 7:
        break

# for y in range(ty + margin + 1):
#     for x in range(tx + margin + 1):
#         region = Region.get(x, y)
#         time = None
#         time_char = None
#         for tool in type_tools[region.type]:
#             state = (x, y, tool)
#             if state in visited and (time == None or visited[state] < time):
#                 time = visited[state]
#                 time_char = chr(timechar[visited[state]])
#                 break
#         else:
#             time_char = region.char()
#         print(time_char, end='')
#     print()

risk = sum(x.type for x in Region.regions.values() if x.x <= tx and x.y <= ty)
print('Part 1:', risk)
print('Part 2:', visited[target_state])

if visited[target_state] >= 987:
    print('too high!')

if visited[target_state] <= 913:
    print('too low!')
