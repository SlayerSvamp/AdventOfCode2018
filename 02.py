import aoc

occurs = aoc.lines(lambda x: set(x.count(c) for c in set(x)))
twos = sum(2 in x for x in occurs)
threes = sum(3 in x for x in occurs)

lines = aoc.lines()
combos = [(a, b) for a in lines for b in lines if a != b]
alike = max(combos, key=lambda combo: sum(a == b for a, b in zip(*combo)))
common = ''.join(a for a, b in zip(*alike) if a == b)

print('Part One:', twos * threes)
print('Part Two:', common)
