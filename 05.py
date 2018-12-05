from aoc import raw as polymer


def react(string):
    def opposites(a, b): return ord(a) ^ ord(b) == 32
    for i in range(len(string) - 1, 0, -1):
        if i < len(string) and opposites(*string[i-1:i+1]):
            string = string[:i-1] + string[i+1:]
    return string


print('Part One:', len(react(polymer)))

units = set(x.lower() for x in polymer)
lengths = []
for c in set(polymer.lower()):
    improved = ''.join(filter(lambda x: x.lower() != c, polymer))
    reacted = react(improved)
    lengths.append(len(reacted))

print('Part Two:', min(lengths))
