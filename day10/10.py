with open('input.txt') as f:
    inp = f.read()

inp = [int(i) for i in inp.splitlines()]
inp = [0] + inp + [max(inp) + 3]
inp.sort()
diffs = [0, 0, 0]

for i in range(len(inp) - 1):
    d = inp[i + 1] - inp[i]
    diffs[d - 1] += 1

print(diffs[0] * diffs[2])

dyn = {}

def ways(ads):
    if len(ads) in dyn:
        return(dyn[len(ads)])
    if len(ads) <= 1:
        return 1
    i = 1
    tot = 0
    while i < len(ads) and ads[i] <= ads[0] + 3:
        tot += ways(ads[i:])
        i += 1
    dyn[len(ads)] = tot
    return tot

print(ways(inp))
