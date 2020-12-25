with open('input.txt') as f:
    inp = f.read()

inp = inp.splitlines()



# Idea: it doesn't matter in which order you take the steps (e.g. E, SE or SE, E), you end up in the same place.
# Count SE, SW, NE, and NW as 1 step north-west, one step east-west.
# And count E, W as 2 steps east-west.


def parse_instr(line):
    i = 0
    res = []
    while i < len(line):
        if line[i] == 'e':
            res.append('e')
        elif line[i:i+2] == 'se':
            res.append('se')
            i += 1
        elif line[i:i+2] == 'sw':
            res.append('sw')
            i += 1
        elif line[i] == 'w':
            res.append('w')
        elif line[i:i+2] == 'nw':
            res.append('nw')
            i += 1
        elif line[i:i+2] == 'ne':
            res.append('ne')
            i += 1
        else:
            raise ValueError(line, i, line[i:i+2])
        i+=1
    return res


def instr_to_loc(i):
    ew = 0
    ns = 0
    for x in i:
        if x == 'e':
            ew += 2
        elif x == 'w':
            ew -= 2
        elif x == 'ne':
            ew += 1
            ns += 1
        elif x == 'nw':
            ew -= 1
            ns += 1
        elif x == 'se':
            ew += 1
            ns -= 1
        elif x == 'sw':
            ew -= 1
            ns -= 1
        else:
            raise ValueError()
    return ew, ns


instrs = [ parse_instr(l) for l in inp ]

for i in range(len(instrs)):
    instrs[i].sort()

blacks = set()

for x in instrs:
    x = instr_to_loc(x)
    if x in blacks:
        blacks.remove(x)
    else:
        blacks.add(x)

print(len(blacks))

# Part 2

def update_tiles(blacks):
    res = set()
    adjacents = [ (2, 0), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1) ]
    relevant_whites = set()
    for (ew, ns) in blacks:
        black_neighs = 0
        for (dew, dns) in adjacents:
            neigh = (ew + dew, ns + dns)
            if neigh in blacks:
                black_neighs += 1
            else:
                relevant_whites.add(neigh)
        if 1 <= black_neighs <= 2:
            # Remain black.
            res.add((ew, ns))
    for (ew, ns) in relevant_whites:
        black_neighs = 0
        for (dew, dns) in adjacents:
            neigh = (ew + dew, ns + dns)
            if neigh in blacks:
                black_neighs += 1
        if black_neighs == 2:
            # Flip to black.
            res.add((ew, ns))
    return res


for _ in range(100):
    blacks = update_tiles(blacks)

print(len(blacks))
