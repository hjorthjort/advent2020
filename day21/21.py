with open('input.txt') as f:
    inp = f.read()

inp_ls = inp.splitlines()

foods = []
cands = {}
all_ingrs = set()

for l in inp_ls:
    [ingrs, allers] = l.split(' (contains ')
    ingrs = set(ingrs.split(' '))
    all_ingrs = all_ingrs.union(ingrs)
    allers = allers[:-1].split(', ')
    foods.append((ingrs, allers))
    for a in allers:
        if a not in cands:
            cands[a] = ingrs
        else:
            cands[a] = cands[a].intersection(ingrs)


# List of all ingredients which could be an allergen.
cands_list = list(cands.items())
cands_list.sort(key=lambda t: len(t[1]))

for i in range(len(cands_list)):
    (f, a) = cands_list[i]
    assert len(a) == 1
    for j in range(i+1, len(cands_list)):
        (f2, a2) = cands_list[j]
        cands_list[j] = (f2, a2.difference(a))

non_allers = all_ingrs.difference(set(i for s in map(lambda x: x[1], cands_list) for i in s))

res = 0
for (f, _) in foods:
    for n in non_allers:
        if n in f:
            res += 1

print(res)

# Part 2

cands_list.sort(key=lambda x: x[0])
res = ','.join(map(lambda x: x[1].pop(), cands_list))

print(res)
