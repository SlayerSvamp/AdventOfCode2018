import aoc

dimensions = {'min-y': 0, 'min-x': 0, 'y': 0, 'x': 0}
ranges = []
for line in aoc.lines():
    pos, span = line.split(', ')
    static_key, static_value = pos.split('=')
    static_value = int(static_value)
    range_key, range_values = span.split('=')
    range_tuple = tuple(int(x) for x in range_values.split('..'))

    ranges.append(((static_key, static_value), (range_key, range_tuple)))

    if static_value < dimensions['min-' + static_key]:
        dimensions['min-' + static_key] = static_value

    if range_tuple[1] < dimensions['min-' + range_key]:
        dimensions['min-' + range_key] = range_tuple[1]

    if static_value > dimensions[static_key]:
        dimensions[static_key] = static_value

    if range_tuple[1] > dimensions[range_key]:
        dimensions[range_key] = range_tuple[1]

grid = dict(((x, y), '.') for y in range(dimensions['min-y'], dimensions['y'] + 1) for x in range(dimensions['min-x'],dimensions['x'] + 1))

def get_range(z):
    if isinstance(z, tuple):
        return range(*z)
    return range(z, z + 1)

for (k1, v1), (k2, v2) in ranges:
    dims = {k1 : get_range(v1), k2 : get_range(v2)}
    for y in dims['y']:
        for x in dims['x']:
            grid[x,y] = '#'

for y in range(dimensions['min-y'], dimensions['y'] + 1):
    row = ''
    for x in range(dimensions['min-x'],dimensions['x'] + 1):
        row += grid[x,y]
    print(row)
