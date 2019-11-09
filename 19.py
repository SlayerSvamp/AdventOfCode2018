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
    return (registers[0])


def simplified(part):
    # manually rewrote the "assembly code" to readable code,
    # then removed unnessecary complexity to get to the essential resulting code
    # aka: sum all values by which the limit is evenly divisible 
    limit = 931 if part == 1 else 10551331
    return sum(x for x in range(1, limit + 1) if (limit % x) == 0)

    
    # a = 0
    # f = 931 if part == 1 else 10551331

    # while True:
    #     b = 1
    #     while True:
    #         e = 1
    #         while e <= f:
    #             if b * e == f:
    #                 a += b
    #             e += 1
    #         b += 1
    #         if b > f:
    #             return a

    # ip 2
    # 0  cur += 16
    # 1  b = 1
    # 2  e = 1
    # 3  d = b * e
    # 4  d = d == f
    # 5  cur += d
    # 6  cur += 1
    # 7  a += b
    # 8  e += 1
    # 9  d = e > f
    # 10 cur += d
    # 11 cur = 2
    # 12 b += 1
    # 13 d = b > f
    # 14 cur += d
    # 15 cur = 1
    # 16 cur *= cur
    # 17 f += 2
    # 18 f *= f
    # 19 f *= cur
    # 20 f *= 11
    # 21 d += 4
    # 22 d *= cur
    # 23 d += 7
    # 24 f += d
    # 25 cur += a
    # 26 cur = 0
    # 27 d = cur
    # 28 d *= cur
    # 29 d += cur
    # 30 d *= cur
    # 31 d *= 14
    # 32 d *= cur
    # 33 f += d
    # 34 a = 0
    # 35 cur = 0


# part1 = runner([0, 0, 0, 0, 0, 0])
# print('Part One:', part1)

print('Part One:', simplified(1))
print('Part Two:', simplified(2))
