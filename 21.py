# occuring check is faster with sets
visited = set()
# accessing first and last occurance is easier with lists
ordered = list()

f = 0
while True:
    b = f | 65536
    f = 10678677
    while True:
        f += b & 255
        # f &= 16777215
        f *= 65899
        f &= 16777215
        if 256 > b:
            break
        b >>= 8
    if f in visited:
        break
    ordered.append(f)
    visited.add(f)

print('Part 1:', ordered[0])
print('Part 2:', ordered[-1])

# ####  step one  ##############################
# 0, 1, 2, 3, 4, 5
# a, b, c, d, e, f = ?, 0, 0, 0, 0, 0

# # ip 2
# f = 123  # seti 123 0 5
# f &= 456  # bani 5 456 5
# f = f == 72  # eqri 5 72 5
# c += f  # addr 5 2 2
# c = 0  # seti 0 0 2
# f = 0  # seti 0 4 5
# b = f | 65536  # bori 5 65536 1
# f = 10678677  # seti 10678677 3 5
# e = b & 255  # bani 1 255 4
# f += e  # addr 5 4 5
# f &= 16777215  # bani 5 16777215 5
# f *= 65899  # muli 5 65899 5
# f &= 16777215  # bani 5 16777215 5
# e = 256 > b  # gtir 256 1 4
# c += e  # addr 4 2 2
# c += 1  # addi 2 1 2
# c = 27  # seti 27 5 2
# e = 0  # seti 0 6 4
# d = e + 1  # addi 4 1 3
# d *= 256  # muli 3 256 3
# d = d > b  # gtrr 3 1 3
# c += d  # addr 3 2 2
# c += 1  # addi 2 1 2
# c = 25  # seti 25 4 2
# e += 1  # addi 4 1 4
# c = 17  # seti 17 6 2
# b = e  # setr 4 6 1
# c = 7  # seti 7 5 2
# e = f == a  # eqrr 5 0 4
# c += e  # addr 4 2 2
# c = 5  # seti 5 4 2
