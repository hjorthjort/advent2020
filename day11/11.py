from copy import deepcopy

with open('input.txt') as f:
    inp = f.read()

arounds1 = {}


def around1(pos_x, pos_y, max_x, max_y):
    if (pos_x, pos_y) in arounds1:
        return arounds1[(pos_x, pos_y)]
    positions = [(x, y) for x in range(pos_x-1, pos_x+2) for y in range(pos_y-1, pos_y+2) if max_x > x >= 0 and max_y > y >= 0 and not (x == pos_x and y == pos_y) ]
    arounds1[(pos_x, pos_y)] = positions
    return positions

def main(tolerance, around):
    grid = inp.splitlines()
    grid = [ [c for c in s] for s in grid]

    new = deepcopy(grid)

    unstable = True
    while unstable:
        unstable = False
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                a = around(x, y, len(grid[y]), len(grid))
                curr = grid[y][x]
                status = [grid[y][x] for (x,y) in a]
                occ = status.count('#')
                free = status.count('L')
                if curr == '.':
                    pass
                elif occ == 0 and curr == 'L':
                    new[y][x] = '#'
                    unstable = True
                elif occ >= tolerance and curr == '#':
                    new[y][x] = 'L'
                    unstable = True
        grid = new
        new = deepcopy(grid)

    tot = 0
    for l in grid:
        tot += l.count('#')
    print(tot)

main(4, around1)

arounds2 = {}
ds = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]
grid = inp.splitlines()
def around2(x, y, max_x, max_y):
    if (x, y) in arounds2:
        return arounds2[(x,y)]
    positions = []
    (cx, cy) = (x, y)
    for (dx, dy) in ds:
        (cx, cy) = (x + dx, y + dy)
        while 0 <= cx < max_x and 0 <= cy < max_y:
            if not grid[cy][cx] == '.':
                positions.append((cx, cy))
                break
            cx += dx
            cy += dy
    arounds2[(x, y)] = positions
    return positions

main(5, around2)
