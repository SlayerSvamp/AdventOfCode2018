GRID_SIZE = 300
GRID_SERIAL_NUMBER = 6392


def get_grid(serial):
    def get_power_level(x, y):
        rackID = x + 10
        power = rackID * y + serial
        power *= rackID / 100
        return int(power) % 10 - 5
    return [[get_power_level(x - 1, y - 1) for y in range(1, GRID_SIZE + 1)] for x in range(1, GRID_SIZE + 1)]


def get_max(grid, size):
    def snd(x): return x[1]
    subgrids = (((x, y), sum_subgrid(grid, x, y, size))
                for y in range(1, GRID_SIZE+2-size) for x in range(1, GRID_SIZE+2-size))
    max_val = max(subgrids, key=snd)
    return max_val


def sum_subgrid(grid, x, y, size):
    tot = 0
    for xx in grid[x:x+size]:
        tot += sum(xx[y:y+size])
    return tot


grid = get_grid(GRID_SERIAL_NUMBER)
(p1_x, p1_y), p1_size = get_max(grid, 3)

print(f'Part One: {p1_x},{p1_y}')

p2_size = p1_size
tot = 0
for size in range(1, GRID_SIZE + 1):
    this, this_tot = get_max(grid, size)
    if tot < this_tot:
        print(
            f'Part Two: {this[0]},{this[1]},{size} with value {this_tot} (work in progress)       ', end='\r')
        p2_size = size
        tot = this_tot
        p2_x, p2_y = this

print(f'Part Two: {p2_x},{p2_y},{p2_size}                                    ')
print('Done!')
