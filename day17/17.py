with open('input.txt') as f:
    inp = f.read()

inp = inp.split('\n')

pd = set()

z = 0
for x in range(len(inp)):
    for y in range(len(inp[x])):
        if inp[x][y] == '#':
            pd.add((x,y,z))


def n1(a):
    return range(a-1, a+2)


def neighs(p):
    (x, y, z) = p
    return [(a,b,c) for a in n1(x) for b in n1(y) for c in n1(z) if (a, b, c) != (x, y, z)]


def main(pd, neighs):
    cycles = 6
    for i in range(cycles):
        counts = { p: 0 for p in pd }
        for p in pd:
            for n in neighs(p):
                if n in counts:
                    counts[n] += 1
                else:
                    counts[n] = 1

        for (p, c) in counts.items():
            if p in pd:
                if not (2 <= c <= 3):
                    pd.remove(p)
            else:
                if c == 3:
                    pd.add(p)
    return (len(list(pd)))

print(main(pd, neighs))

# Part 2

pd = set()

z = 0
w = 0
for x in range(len(inp)):
    for y in range(len(inp[x])):
        if inp[x][y] == '#':
            pd.add((x,y,z,w))


def neighs(p):
    (x, y, z, w) = p
    res = [(a,b,c,d) for a in n1(x) for b in n1(y) for c in n1(z) for d in n1(w) if (a, b, c, d) != p]
    return res

print(main(pd, neighs))
