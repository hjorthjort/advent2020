from math import gcd

with open('input.txt') as f:
    inp = f.read()

inp = inp.splitlines()
start = int(inp[0])
bus_times = [ int(x) if x != 'x' else 'x' for x in inp[1].split(',')]
buses = [x for x in bus_times if x != 'x']

def find_next():
    i = 0
    while True:
        for b in buses:
            if (start + i) % b == 0:
                return (i, b)
        i += 1

(wait, next_bus) = find_next()
print(wait*next_bus)

# Part 2

bt = [(x, -bus_times.index(x)) for x in bus_times if x != 'x']


def chinese_pair(a1, n1, a2, n2):
    assert gcd(n1, n2) == 1, (n1, n2)
    if n1 < n2:
        return chinese_pair(a2, n2, a1, n1)
    a1 %= n1
    a2 %= n2
    for i in range(a1, n1 * n2, n1):
        if i % n2 == a2 and i % n1 == a1:
            return i, n1*n2
    raise Exception("%d mod %d and %d mod %d" % (a1, n1, a2, n2))


(n1, a1) = bt[0]
for (n2, a2) in bt[1:]:
    (a1, n1) = chinese_pair(a1, n1, a2, n2)

print(a1)
