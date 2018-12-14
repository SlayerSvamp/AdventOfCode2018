import aoc


class Cart():
    DIR = dict([(0, (0, -1)), (1, (1, 0)), (2, (0, 1)), (3, (-1, 0))])

    def __init__(self, pos, arrow):
        self.pos = pos
        self.facing = '^>v<'.find(arrow)
        self.turned = 0

    def move(self):
        (x, y) = self.pos
        dx, dy = self.DIR[self.facing]
        self.pos = (x+dx, y+dy)

    def turn(self, track):
        if track in '\\/+':
            if track in '\\/':
                if (self.facing % 2) ^ (track == '/'):
                    self.facing += 1
                else:
                    self.facing += 3
            elif track == '+':
                self.facing += [3, 0, 1][self.turned]
                self.turned = (self.turned+1) % 3
            self.facing %= 4

    def crashed(self, carts):
        return next((c for c in carts if c.pos == cart.pos and c != self), None)

    def __repr__(self, *args):
        return ', '.join([str(self.pos), str(self.facing), str(self.turned)])


system = {}
carts = []
for y, row in enumerate(aoc.lines()):
    for x, cell in enumerate(row):
        system[x, y] = cell
        if cell in '<>^v':
            carts.append(Cart((x, y), cell))

first_crash_at = None
while len(carts) > 1:
    for cart in sorted(carts, key=lambda x: x.pos[::-1]):
        if cart in carts:
            cart.move()
            cart.turn(system[cart.pos])

            crashed_cart = cart.crashed(carts)
            if crashed_cart:
                if not first_crash_at:
                    first_crash_at = cart.pos
                carts.remove(crashed_cart)
                carts.remove(cart)

print('Part One:', ','.join(map(str, first_crash_at)))
print('Part Two:', ','.join(map(str, carts[0].pos)))
