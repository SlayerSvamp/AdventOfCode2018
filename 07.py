import aoc
from itertools import count


def reset():
    global left, done
    left = dict((p, set(a for a, b in instr if p == b)) for p in parts)
    done = ''


def avail():
    return sorted(x for x in left if all(z in done for z in left[x]))


instr = [(x[1], x[7]) for x in aoc.splitted_lines()]
parts = set([a for a, _ in instr] + [b for _, b in instr])
reset()

while left:
    nxt = avail()[0]
    done += nxt
    del left[nxt]

alone = done

reset()
worker = {}
for second in count():
    for w in list(worker):
        if worker[w] == second:
            del worker[w]
            done += w

    while avail() and len(worker) < 5:  # 4 elfs + you
        nxt = avail()[0]
        worker[nxt] = second + ord(nxt) - 4  # ord - 64 + 60 seconds
        del left[nxt]

    if not worker:
        break

print('Part One:', alone)
print('Part Two:', second)
