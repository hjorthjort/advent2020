from functools import reduce

with open('input.txt') as f:
    inp = f.read()

inp = inp.split('\n\n')
groups = [ i.splitlines() for i in inp]

g_ans = []
for g in groups:
    a = []
    for ans in g:
        s = set()
        for c in ans:
            s.add(c)
        a.append(s)
    g_ans.append(a)

tot_any = 0

print(sum(map(len, [reduce(lambda x, y: x.union(y),        xs, set()) for xs in g_ans])))
print(sum(map(len, [reduce(lambda x, y: x.intersection(y), xs, xs[0]) for xs in g_ans])))
