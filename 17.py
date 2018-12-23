import aoc

grid = dict()

for static_key, static_value, _, range_from, range_to in aoc.splitted_lines(regex=', |=|[.]{2}'):
    for range_value in range(int(range_from), int(range_to) + 1):
        pos = (int(static_value), range_value)
        if static_key == 'y':
            pos = pos[::-1]
        grid[pos] = '#'


min_y, *_, max_y = sorted(y for (_, y), c in grid.items() if c == '#')


def from_grid(x, y):
    return grid.get((x, y), '.')


def has_support(x, y):
    def inner(direction, x, y):
        while from_grid(x, y) != '#':
            if from_grid(x, y + 1) in '|.':
                return False
            x += direction
        return True
    return inner(-1, x-1, y) and inner(1, x, y)


def fill(x, y):
    def inner(direction, x, y):
        while from_grid(x, y) != '#':
            grid[x, y] = '~'
            x += direction
    inner(-1, x-1, y)
    inner(1, x, y)


def flow(x, y):
    def inner(direction, x, y):
        while from_grid(x, y) != '#':
            grid[x, y] = '|'
            if from_grid(x, y+1) in '.|':
                yield (x, y)
                break
            x += direction
    return [*inner(-1, x, y), *inner(1, x, y)]


def pour(x, y):
    while from_grid(x, y + 1) == '.':
        y += 1
        grid[x, y] = '|'
        if y+1 > max_y:
            break
    else:
        if from_grid(x, y+1) == '|':
            return
        while has_support(x, y):
            fill(x, y)
            y -= 1
        for x, y in flow(x, y):
            pour(x, y)


spring = (500, 0)
pour(*spring)
print('Part One:', sum(c in '~|' for (_, y), c in grid.items() if y >= min_y))
print('Part Two:', sum(c == '~' for (_, y), c in grid.items() if y >= min_y))
