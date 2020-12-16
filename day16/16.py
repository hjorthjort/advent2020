with open('input.txt') as f:
    inp = f.read()


inp = inp.split('\n\n')

rules = inp[0].splitlines()
near = [[int(x) for x in l.split(',')] for l in inp[2].splitlines()[1:]]


def parse_rules(lines):
    no_desc = [l.split(': ')[1] for l in lines]
    no_or = [l.split(' or ') for l in no_desc]
    parsed = [[[int(x) for x in r.split('-')] for r in l] for l in no_or]
    ranges = [[(int(lo), int(hi)) for [lo, hi] in ranges] for ranges in parsed]

    return ranges


rules = parse_rules(rules)
ranges = [r for ranges in rules for r in ranges]


def invalid(x, ranges):
    return all([not (lo <= x <= hi) for (lo, hi) in ranges])


invs = [x for l in near for x in l if invalid(x, ranges)]
print(sum(invs))

# Part 2.

valids = [n for n in near if not any(map(lambda x: invalid(x, ranges), n))]
your = [ int(x) for x in inp[1].splitlines()[1].split(',')  ]


def matching(vals, rules):
    res = []
    for i in range(len(rules)):
        r = rules[i]
        if not any(map(lambda x: invalid(x, r), vals)):
            res.append(i)
    return res

field_matches = []

for i in range(len(valids[0])):
    vals = [v[i] for v in valids]
    match = matching(vals, rules)
    field_matches.append((i, match))

field_matches.sort(key=lambda x: len(x[1]))

r2i = {}

for (i, ms) in field_matches:
    [m] = [m for m in ms if m not in r2i.keys()]
    r2i[m] = i

print(r2i)

ans = 1
dep_max = 5
print(your)
for (r, i) in r2i.items():
    if r <= dep_max:
        ans *= your[i]

print(ans)
