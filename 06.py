import aoc

points = aoc.splitted_lines(int, ', ')
points = set((x, y) for x, y in points)


def boundry(side, dir):
    direction = dir == 'y'
    return side(points, key=lambda x: x[direction])[direction]


left = boundry(min, 'x')
right = boundry(max, 'x')
top = boundry(min, 'y')
bottom = boundry(max, 'y')
coords = dict.fromkeys(points, 0)
infs = set()
within_10_000 = 0

for x in range(left, right):
    for y in range(top, bottom):
        def diff(point):
            return abs(point[0] - x) + abs(point[1] - y)

        distances = [(point, diff(point)) for point in points]
        within_10_000 += sum(diff for _, diff in distances) < 10_000
        (a_point, a_diff), (_, b_diff) = sorted(distances, key=lambda z: z[1])[:2]

        if a_diff < b_diff:
            if x in (left, right-1) or y in (top, bottom-1):
                infs.add(a_point)
            else:
                coords[a_point] += 1

print('Part One:', max(coords[key] for key in set(coords) - infs))
print('Part Two:', within_10_000)
