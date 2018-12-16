import aoc

DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def set_hp(char): return 201 if char == 'E' else -201 if char == 'G' else 0


cave = dict(((y, x), set_hp(cell))
            for y, row in enumerate(aoc.lines(enumerate))
            for x, cell in row if cell != '#')


def get_units(predicate):
    return sorted([pos for pos, unit in cave.items() if predicate(unit)])


def space(unit): return unit == 0


def elf(unit): return unit > 0


def goblin(unit): return unit < 0


def enemy(unit): return goblin if unit > 0 else elf


def non_space(unit): return unit


def get_surr(pos): return set(
    p for p in [(pos[0]+dy, pos[1]+dx) for dy, dx in DIR] if p in cave)


rounds = 0
while get_units(elf) and get_units(goblin):
    for pos in get_units(non_space):
        if not get_units(elf) or not get_units(goblin):
            break
        y, x = pos
        if not cave[pos]:
            continue
        enemies = get_units(enemy(cave[pos]))
        if not any([z for z in enemies if z in get_surr(pos)]):
            candidates = set()
            seen = set(enemies)
            last_range = set(seen)
            while last_range:
                new_range = set()
                for p in last_range:
                    surr = get_surr(p) - seen
                    if pos in surr:
                        candidates.add(p)
                    
                    new_range |= surr - set(get_units(non_space))

                seen |= new_range

                if candidates:
                    break                
                last_range = new_range
            else:
                continue

            move_to = sorted(candidates)[0]
            cave[move_to] = cave[pos]
            cave[pos] = 0
            pos = move_to

        in_combat = sorted((z for z in enemies if z in get_surr(pos)), key=lambda x: (cave[x], *x), reverse=True)
        if in_combat:
            if not cave[pos]:
                continue
            # hit for 3 attack power
            power = 3 if cave[pos] < 0 else -3
            cave[in_combat[0]] -= power
    else:
        rounds += 1
        continue
    
    for y in range(len(aoc.lines())):
        row = ''
        for x in range(len(aoc.lines()[0])):
            if (y, x) in cave:
                val = cave[y, x]
                row += 'G' if val < 0 else 'E' if val else '.'
            else:
                row += '#'
        print(row, *[cave[z] for z in get_units(non_space) if z[0] == y])
        
    print('rounds', rounds, 'passed')
    print()

# 5527 is too low
# 596916 too high
# 194656 too high
# 192128 wrong answer (don't know if high or low)
tot_hp = sum(abs(cave[x])-1 for x in get_units(non_space))
print('tot_hp', tot_hp)
print('Part One:', rounds * tot_hp)
