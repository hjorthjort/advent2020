with open('input.txt') as f:
    inp = f.read()

inp = inp.split('\n')

pd = set()

z = 0
for x in range(len(inp)):
    for y in range(len(inp[x])):
        if inp[x][y] == '#':
            pd.add((x,y,z))

def neighs(p):
    def n1(a):
        return range(a-1, a+2)

    (x, y, z) = p
    return [(a,b,c) for a in n1(x) for b in n1(y) for c in n1(z) if (a, b, c) != (x, y, z)]

def main(pd, neighs):
    cycles = 6
    for i in range(cycles):
        consider = set()
        for p in pd:
            consider.add(p)
            for n in neighs(p):
                consider.add(n)

        on = set()
        off = set()
        for p in consider:
            # Active.
            ns = neighs(p)
            act = len([x for x in ns if x in pd])
            if p in pd:
                if not (2 <= act <= 3):
                    off.add(p)
            else:
                if act == 3:
                    on.add(p)
        pd = pd.union(on)
        pd = pd.difference(off)

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
    def n1(a):
        return range(a-1, a+2)

    (x, y, z, w) = p
    return [(a,b,c,d) for a in n1(x) for b in n1(y) for c in n1(z) for d in n1(w) if (a, b, c, d) != p]

print(main(pd, neighs))
