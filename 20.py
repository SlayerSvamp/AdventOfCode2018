from aoc import raw
from colorama import init, Fore

init()
opposite = {
    'E': 'W',
    'N': 'S',
    'S': 'N',
    'W': 'E',
}
pipes = {
    'E': '<',
    'N': 'v',
    'S': '^',
    'W': '>',
    'EN': '╚',
    'NS': '║',
    'NW': '╝',
    'ES': '╔',
    'EW': '═',
    'SW': '╗',
    'ENS': '╠',
    'ENW': '╩',
    'ESW': '╦',
    'NSW': '╣',
    'ENSW': '╬',
}
x, y = 0, 0
rooms = {(x, y): {'doors': '', 'value': 0, 'distant': False}}
roots = [(x, y), ]
for c in raw:
    if c in 'NEWS':
        new = {
            'S': (x, y-1),
            'N': (x, y+1),
            'W': (x-1, y),
            'E': (x+1, y),
        }[c]
        if new not in rooms:
            rooms[new] = {'doors': '', 'value': rooms[(x, y)]['value'] + 1}
            rooms[new]['distant'] = rooms[new]['value'] > 999
        rooms[new]['doors'] += opposite[c]
        rooms[(x, y)]['doors'] += c
        x, y = new
    if c in '(':
        roots.append((x, y))
    if c in ')':
        x, y = roots[-1]
        del roots[-1]
    if c in '|':
        x, y = roots[-1]
    if c in '$':
        break


most_distant_room = max(x['value'] for x in rooms.values())
number_of_distant_rooms = sum(1 for x in rooms.values() if x['distant'])


def draw():
    min_x = min(v for (v, _) in rooms)
    min_y = min(v for (_, v) in rooms)
    max_x = max(v for (v, _) in rooms)
    max_y = max(v for (_, v) in rooms)
    for y in range(min_y, max_y+1)[::-1]:
        for x in range(min_x, max_x+1):
            if (x, y) == (0, 0):
                character = 'X'
                fore = Fore.YELLOW
            else:
                fore = Fore.WHITE
                character = pipes[''.join(sorted(set(rooms[(x, y)]['doors'])))]
                if rooms[(x, y)]['value'] == most_distant_room:
                    fore = Fore.RED
                elif rooms[(x, y)]['distant']:
                    fore = Fore.BLUE

            print(fore + character, end=Fore.WHITE)
        print()


draw()
print('Part 1:', most_distant_room)
print('Part 2:', number_of_distant_rooms)
