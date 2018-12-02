import aoc


def occurs(string):
    return set(sum(c == x for x in string) for c in set(string))


occ = aoc.lines(occurs)
twos = sum(2 in x for x in occ)
threes = sum(3 in x for x in occ)

lines = aoc.lines()
id_count = len(lines)
id_length = len(lines[0])

for i in range(id_length):
    compares = [x[:i] + x[i+1:] for x in lines]
    if len(set(compares)) < id_count:
        z = zip(sorted(compares), sorted(set(compares)))
        common = next(c for c, x in z if x != c)

print('Part One:', twos * threes)
print('Part Two:', common)
