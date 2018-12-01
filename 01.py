from itertools import cycle
import aoc

sequence = aoc.lines(int)
frequency = 0
reached = set()

for x in cycle(sequence):
    reached.add(frequency)
    frequency += x
    if frequency in reached:
        break

print('Part One:', sum(sequence))
print('Part Two:', frequency)
