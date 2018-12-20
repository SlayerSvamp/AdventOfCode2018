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


samples = []
curr = None
sample_lines, data_lines = [x.splitlines() for x in aoc.raw.split('\n\n\n\n')]
data = [[int(y) for y in x.split()] for x in data_lines]

# parse samples
for line in sample_lines:
    if 'f' in line:
        b = line.split('[')[1][:-1]
        d = [int(x) for x in b.split(', ')]
        if line.startswith('Before'):
            curr = [d]
        else:
            curr.append(d)
            samples.append(curr)
    elif line:
        curr.append([int(x) for x in line.split()])

# create key references
keys = {}
for opcode in set(x for _, (x, *_), _ in samples):
    for tool in tools:
        if all(act(tool, list(reg), *args) == after for reg, (action, *args), after in samples if action == opcode):
            if opcode not in keys:
                keys[opcode] = []
            keys[opcode].append(tool)

# remove false key references
while any(y for x, *y in keys.values()):
    for lone, *rest in keys.values():
        if not rest:
            for key in keys:
                if lone in keys[key] and len(keys[key]) - 1:
                    keys[key].remove(lone)

# replace key lists with keys
for val in set(keys):
    keys[val] = keys[val][0]

# calc part 1
ambiguous = 0
for before, (tool, *args), after in samples:
    occurs = 0
    for tool in tools:
        if act(tool, list(before), *args) == after:
            occurs += 1
    if occurs >= 3:
        ambiguous += 1

# run data for part 2
registers = [0, 0, 0, 0]
for tool, *args in data:
    key = keys[tool]
    act(key, registers, *args)

print('Part One:', ambiguous)
print('Part Two:', registers[0])
