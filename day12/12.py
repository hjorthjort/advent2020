with open('input.txt') as f:
    inp = f.read()

inp = inp.splitlines()
inp = [ (x[0], int(x[1:])) for x in inp]


def rotate(d, direction, deg):
    for i in range(deg//90):
        if direction == 'R':
            d = (d[1], d[0] * -1)
        if direction == 'L':
            d = (-1* d[1], d[0])
    return d

px = 0
py = 0
d = (1, 0)
for (i, v) in inp:
    if i == 'F':
        px += d[0] * v
        py += d[1] * v
    elif i == 'E':
        px += v
    elif i == 'N':
        py += v
    elif i == 'W':
        px -= v
    elif i == 'S':
        py -= v
    else:
        d = rotate(d, i, v)
print(abs(px) + abs(py))


px = 0
py = 0
d = (10, 1)
for (i, v) in inp:
    if i == 'F':
        px += d[0] * v
        py += d[1] * v
    elif i == 'E':
        d = (d[0] + v, d[1])
    elif i == 'N':
        d = (d[0], d[1] + v)
    elif i == 'W':
        d = (d[0] - v, d[1])
    elif i == 'S':
        d = (d[0], d[1] - v)
    else:
        d = rotate(d, i, v)

print(abs(px) + abs(py))
