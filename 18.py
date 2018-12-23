import aoc

SIZE = len(aoc.lines())
LUMBER, TREES, OPEN = '#|.'


def adjacent(state, x, y):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx != 0 or dy != 0:
                ret = state.get((x+dx, y+dy), None)
                if ret:
                    yield ret


def fell(state, seconds):
    seen = []
    curr = dict(state)
    for second in range(seconds):
        new = {}
        for y in range(SIZE):
            for x in range(SIZE):
                adj = list(adjacent(curr, x, y))
                if curr[x, y] == OPEN and adj.count(TREES) >= 3:
                    new[x, y] = TREES
                elif curr[x, y] == TREES and adj.count(LUMBER) >= 3:
                    new[x, y] = LUMBER
                elif curr[x, y] == LUMBER and (TREES not in adj or LUMBER not in adj):
                    new[x, y] = OPEN
                else:
                    new[x, y] = curr[x, y]

        state = ''.join(new[x, y] for y in range(SIZE) for x in range(SIZE))
        if state in seen:
            loop = seen[seen.index(state):]
            print(loop[0] == state)
            left = seconds - second - 1
            return loop[left % len(loop)]
        seen.append(state)
        curr = new
    return state


initial = dict(((x, y), cell) for y, row in enumerate(aoc.lines())
               for x, cell in enumerate(row))

acres = fell(initial, 10)
print('Part One:', acres.count(LUMBER) * acres.count(TREES))
acres = fell(initial, 1000_000_000)
print('Part Two:', acres.count(LUMBER) * acres.count(TREES))
