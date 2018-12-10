import aoc
from itertools import count


def parse_point(string):
    splitted = string.replace(' ', '').split('<')
    position, _ = splitted[1].split('>')
    velocity, _ = splitted[2].split('>')
    x, y = [int(z) for z in position.split(',')]
    dx, dy = [int(z) for z in velocity.split(',')]
    return ((x, y), (dx, dy))


def point_after_n_seconds(point, n):
    (x, y), (dx, dy) = point
    return (x + dx * n, y + dy * n)


def print_message(message):
    left = min(x for x, _ in message) - 1
    top = min(y for _, y in message)
    right = max(x for x, _ in message) + 2
    bottom = max(y for _, y in message) + 1

    for y in range(top, bottom):
        row = [' '] * (right - left)
        for x in range(left, right):
            if (x, y) in message:
                row[x - left] = '█'
        print(''.join(row))


points = aoc.lines(parse_point)
last_width = None
last = None

for second in count():
    message = []
    for point in points:
        message.append(point_after_n_seconds(point, second))
    width = max(x for x, _ in message) - min(x for x, _ in message)
    if last_width != None and width > last_width:
        break
    else:
        last_width = width
        last = message

print('Part One:')
print_message(last)
print('Part Two:', second - 1)
