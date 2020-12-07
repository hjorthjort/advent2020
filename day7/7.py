from functools import reduce

with open('input.txt') as f:
    inp = f.read()

inp = inp.splitlines()
d = {}
for l in inp:
    ws = l.split(' ')
    k = ' '.join(ws[0:2])
    cont = l.split(' contain ')[1]
    if cont[0:2] == 'no':
        types = []
    else:
        types = cont.split(', ')
    types = [t.split(' ') for t in types]
    types = [(int(t[0]), ' '.join(t[1:3])) for t in types]

    d[k] = types

reachable = set()
for (k, v) in d.items():
    colors = [x[1] for x in v]
    if 'shiny gold' in colors:
        reachable.add(k)

edited = True
while edited:
    edited = False
    for (k, v) in d.items():
        colors = [x[1] for x in v]
        for c in colors:
            if c in reachable:
                if k not in reachable:
                    reachable.add(k)
                    edited = True

print(len(reachable))

def min_bags(color):
    tot = 0
    for (n, c) in d[color]:
        tot += n + n * min_bags(c)
    return tot

print(min_bags('shiny gold'))
