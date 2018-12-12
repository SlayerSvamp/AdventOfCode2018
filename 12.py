import aoc
INITIAL = '##.#.#.##..#....######..#..#...#.#..#.#.#..###.#.#.#..#..###.##.#..#.##.##.#.####..##...##..#..##.#.'
RULES = dict(aoc.lines(lambda x: x.split()[::2]))


def calc_next_gen(current, offset):
    while not current.startswith('....'):
        offset -= 1
        current = '.' + current
    while not current.endswith('....'):
        current += '.'
    next_gen = '..'
    for i in range(2, len(current) - 2):
        next_gen += RULES[current[i-2:i+3]]

    return (next_gen, offset)


def calc_sum_pots(num_gens):
    current = INITIAL
    old_len = diff = left = offset = 0
    for gen in range(num_gens):
        current, offset = calc_next_gen(current, offset)
        curr_len = sum(i + offset for i, x in enumerate(current) if x == '#')
        if diff == curr_len - old_len:
            left = num_gens - gen - 1
            left *= diff
            break
        diff = curr_len - old_len
        old_len = curr_len

    return curr_len + left


print('Part One:', calc_sum_pots(20))
print('Part Two:', calc_sum_pots(50_000_000_000))
