import aoc
from itertools import count
system = {}
for y, row in enumerate(aoc.lines()):
    for x, cell in enumerate(row):
        system[x, y] = cell

DIR = dict([(0, (0, -1)), (1, (1, 0)), (2, (0, 1)), (3, (-1, 0))])
carts = [(key, '^>v<'.find(value), 0) for key, value in system.items() if value in '<>v^']

first_crash = None

for tick in count():
    if len(carts) == 1:
        break
    i = 0
    while i < len(carts):
        (x,y), facing, turned = carts[i]
        dx, dy = DIR[facing]
        pos = (x+dx, y+dy)
        track = system[pos]
        if track in '\\/+':
            if track in '\\/':
                if (facing % 2) ^ (track == '/'):
                    facing += 1
                else:
                    facing += 3
            elif track == '+':
                facing += [3, 0, 1][turned % 3]
                turned += 1
                turned %= 3
            facing %= 4
            
        carts[i] = pos, facing, turned
        crash_carts = [cart for cart in carts if [c for c, *_ in carts].count(cart[0]) > 1]
        if crash_carts:
            if first_crash == None:
                first_crash = crash_carts[0][0]
            diff = 0
            for cart in crash_carts:
                if carts.index(cart) <= i:
                    diff -= 1
                carts.remove(cart)
            i += diff
        i += 1

    # import re
    # for y in range(150):
    #     row = ''
    #     for x in range(150):
    #         if (x,y) not in [c for c, *_ in carts]:
    #             row += re.sub(r'[<^>v]', '.', aoc.lines()[y][x])
    #         else:

    #             row += next('^>v<'[d] for c, d, _ in carts if c == (x,y))
    #     print(row)

    print(carts)


print('Part One:', ','.join(map(str, first_crash)))
print('Part Two:', ','.join(map(str, carts[0][0]))) 
# not 
# 19,28 
# 129,24 
# 12,83