import aoc
from re import findall


def splitter(pattern):
    def inner(line):
        return list(map(int, findall(pattern, line)))
    return inner


sheet = {}
claims = set()

for claim, left, top, width, height in aoc.lines(splitter(r'\d+')):
    claims.add(claim)
    for x in range(left, width + left):
        for y in range(top, height + top):
            if (x, y) not in sheet:
                sheet[x, y] = {claim}
            else:
                sheet[x, y].add(claim)

overlapping_squares = sum(len(c) > 1 for c in sheet.values())
overlapping_claims = set(x for y in sheet.values() if len(y) > 1 for x in y)

print('Part One:', overlapping_squares)
print('Part Two:', claims - overlapping_claims)
