import aoc

current = None
fell_asleep = None
guards = {}

records = aoc.splitted_lines(lambda x: x.strip('[]#'))
sorted_records = sorted(records, key=lambda x: ' '.join(x[:2]))

for _, time, event, guard, *_ in sorted_records:
    if event == 'Guard':
        current = int(guard)
        if current not in guards:
            guards[current] = dict((x, 0) for x in range(60))
    else:
        minute = int(time.split(':')[1])
        if event == 'wakes':
            for x in range(fell_asleep, minute):
                guards[current][x] += 1

        if event == 'falls':
            fell_asleep = minute


def part(part, comparer):
    def compare(x): return comparer(x[1].values())
    sleepy, minutes = max(guards.items(), key=compare)
    chosen_minute = max(minutes.items(), key=lambda x: x[1])[0]
    print(f'Part {part}: {sleepy * chosen_minute}')


part('One', sum)
part('Two', max)
