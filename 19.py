import aoc

tools = {
    'addr': lambda reg, a, b: reg[a] + reg[b],
    'addi': lambda reg, a, b: reg[a] + b,
    'mulr': lambda reg, a, b: reg[a] * reg[b],
    'muli': lambda reg, a, b: reg[a] * b,
    'banr': lambda reg, a, b: reg[a] & reg[b],
    'bani': lambda reg, a, b: reg[a] & b,
    'borr': lambda reg, a, b: reg[a] | reg[b],
    'bori': lambda reg, a, b: reg[a] | b,
    'setr': lambda reg, a, b: reg[a],
    'seti': lambda reg, a, b: a,
    'gtir': lambda reg, a, b: a > reg[b],
    'gtri': lambda reg, a, b: reg[a] > b,
    'gtrr': lambda reg, a, b: reg[a] > reg[b],
    'eqir': lambda reg, a, b: a == reg[b],
    'eqri': lambda reg, a, b: reg[a] == b,
    'eqrr': lambda reg, a, b: reg[a] == reg[b],
}


def act(tool, reg, a, b, c):
    reg[c] = tools[tool](reg, a, b)
    return reg


ip_line, *lines = aoc.splitted_lines()
ip = int(ip_line[1])
data = [[key, *[int(v) for v in values]] for key, *values in lines]


def runner(registers):
    cursor = 0
    while cursor >= 0 and cursor < len(data):
        registers[ip] = cursor
        tool, *args = data[cursor]
        act(tool, registers, *args)
        cursor = registers[ip] + 1
    return registers[0]


part1 = runner([0, 0, 0, 0, 0, 0])
print('Part One:', part1)

part2 = runner([1, 0, 0, 0, 0, 0])
print('Part Two:', part2)
