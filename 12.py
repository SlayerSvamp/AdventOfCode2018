import aoc


def parse_rule(line):
    pattern, _, result = line.split()
    return (pattern, result)


def next_gen(rules, this_gen, offset):
    while not this_gen.startswith('...'):
        offset -= 1
        this_gen = '.' + this_gen
    while not this_gen.endswith('...'):
        this_gen += '.'
    ret = '..'
    for i in range(2, len(this_gen) - 2):
        pattern = this_gen[i-2:i+3] 
        ret += rules.get(pattern, '.')

    return (ret, offset)

def calc_gen(rules, this_gen, gens, offset=0):
    for gen in range(gens):
        if not gen % 1000:
            print('Currently at gen', gen, end='\r')
        this_gen, offset = next_gen(rules, this_gen, offset)
    return (this_gen, offset)

this_gen = '##.#.#.##..#....######..#..#...#.#..#.#.#..###.#.#.#..#..###.##.#..#.##.##.#.####..##...##..#..##.#.'
rules = dict(aoc.lines(parse_rule))



gen, offset = calc_gen(rules, this_gen, 20)
print('Part One:', sum(i+offset for i,x in enumerate(gen) if x == '#'), '                   ')

gen, offset = calc_gen(rules, this_gen, 50_000_000_000)
print('Part Two:', sum(i+offset for i,x in enumerate(gen) if x == '#'),  '                   ')
