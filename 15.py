import aoc

DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]
HP = 200
ATTACK = 3


cave = dict(((y, x), HP if cell == 'E' else -HP if cell == 'G' else 0)
            for y, row in enumerate(aoc.lines(enumerate))
            for x, cell in row if cell != '#')

match_unit = {
    'space': lambda x: x == 0,
    'non_space': lambda x: not not x,
    'elf': lambda x: x > 0,
    'goblin': lambda x: x < 0,
}


def get_units(cave, unit_type):
    return sorted([pos for pos, x in cave.items() if match_unit[unit_type](x)])


def get_surr(cave, pos): return set(
    p for p in [(pos[0]+dy, pos[1]+dx) for dy, dx in DIR] if p in cave)


def fight(cave, elf_attack=3):
    cave = dict(cave)
    elfs_at_start = len(get_units(cave, 'elf'))
    rounds = 0
    while get_units(cave, 'elf') and get_units(cave, 'goblin'):
        for pos in get_units(cave, 'non_space'):
            if not get_units(cave, 'elf') or not get_units(cave, 'goblin'):
                break
            y, x = pos
            hp = cave[pos]
            if not hp:
                continue
            enemies = get_units(cave, 'goblin' if hp > 0 else 'elf')
            if not any([z for z in enemies if z in get_surr(cave, pos)]):
                candidates = set()
                seen = set(enemies)
                last_range = set(seen)
                while last_range:
                    new_range = set()
                    for p in last_range:
                        surr = get_surr(cave, p) - seen
                        if pos in surr:
                            candidates.add(p)

                        new_range |= surr - set(get_units(cave, 'non_space'))

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

            in_combat = sorted((z for z in enemies if z in get_surr(
                cave, pos)), key=lambda x: (abs(cave[x]), *x))
            if in_combat:
                in_combat = in_combat[0]
                if not cave[pos]:
                    continue
                # hit for 3 attack power
                power = ATTACK if cave[pos] < 0 else -elf_attack
                if abs(power) > abs(cave[in_combat]):
                    cave[in_combat] = 0
                else:
                    cave[in_combat] -= power
        else:
            rounds += 1
    tot_hp = sum(abs(cave[x]) for x in get_units(cave, 'non_space'))
    elfs_left = len(get_units(cave, 'elf'))
    return (tot_hp * rounds, elfs_at_start - elfs_left)


elfs_died = True
attack = 2
while elfs_died:
    attack *= 2
    print('Testing', attack,  'attack...')
    score, elfs_died = fight(cave, attack)
    print(elfs_died, 'elfs died.')
new_score = score
while not elfs_died:
    score = new_score
    attack -= 1
    print('Testing', attack,  'attack')
    new_score, elfs_died = fight(cave, attack)
    print(elfs_died, 'elfs died.')

print('Part One:', fight(cave, ATTACK)[0])
print('Part Two:', score)
