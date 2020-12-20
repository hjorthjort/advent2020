import math
from functools import reduce

with open('input.txt') as f:
    inp = f.read()

inp = inp.split('\n\n')

tiles = {}

for g in inp:
    lines = g.splitlines()

    id_tile = int(lines[0].split(' ')[1][:-1])
    tile = lines[1:]
    tiles[id_tile] = tile


def tile2borders(tile):
    b_top = tile[0]
    b_bottom = tile[-1]
    b_left = ''.join([l[0] for l in tile])
    b_right = ''.join([l[-1] for l in tile])
    return b_top, b_bottom, b_left, b_right


borders = {}

for (k, tile) in tiles.items():
    for b in tile2borders(tile):
        if b in borders:
            borders[b].append(k)
        elif b[::-1] in borders:
            borders[b[::-1]].append(k)
        else:
            borders[b] = [k]

edge_tiles = [t[0] for (_, t) in borders.items() if len(t) == 1]
corners = set(t for t in edge_tiles if edge_tiles.count(t) == 2)

print(reduce(lambda x, y: x*y, corners, 1))

# Part 2

def get_neighs(edge):
    if edge in borders:
        return borders[edge]
    return borders[edge[::-1]]

def flip_horiz(tile):
    return [ l[::-1] for l in tile]

def flip_vertic(tile):
    return tile[::-1]

def rot_counter(tile):
    return rot(rot(rot(tile)))

def rot(tile):
    return [ ''.join(x) for x in zip(*tile[::-1]) ]

side = int(math.sqrt(len(tiles)))

img = [[list(corners)[0]]]

# Set up first tile.
curr = img[0][0]
top, bottom, left, right = tile2borders(tiles[curr])
if len(get_neighs(right)) == 1:
    tiles[curr] = flip_horiz(tiles[curr])
if len(get_neighs(bottom)) == 1:
    tiles[curr] = flip_vertic(tiles[curr])


# Fill square.
square = 1
while square < side:
    # Build out the image, keeping it a square the whole time.
    new_row = []
    img.append(new_row)
    curr = img[square - 1][0]
    _, bottom, _, _ = tile2borders(tiles[curr])
    [b_neigh] = [x for x in get_neighs(bottom) if x != curr]
    # print(b_neigh)

    new_row.append(b_neigh)
    btop, bbottom, bleft, bright = tile2borders(tiles[b_neigh])
    if bottom == btop:
        # print('a')
        pass
    elif bottom == btop[::-1]:
        # print('b')
        tiles[b_neigh] = flip_horiz(tiles[b_neigh])
    elif bottom == bbottom:
        # print('c')
        tiles[b_neigh] = flip_vertic(tiles[b_neigh])
    elif bottom == bbottom[::-1]:
        # print('d')
        tiles[b_neigh] = flip_vertic(tiles[b_neigh])
        tiles[b_neigh] = flip_horiz(tiles[b_neigh])
    elif bottom == bright:
        # print('e')
        tiles[b_neigh] = rot_counter(tiles[b_neigh])
    elif bottom == bright[::-1]:
        # print('f')
        tiles[b_neigh] = rot_counter(tiles[b_neigh])
        tiles[b_neigh] = flip_horiz(tiles[b_neigh])
    elif bottom == bleft:
        # print('g')
        tiles[b_neigh] = rot(tiles[b_neigh])
        tiles[b_neigh] = flip_horiz(tiles[b_neigh])
    elif bottom == bleft[::-1]:
        # print('h')
        tiles[b_neigh] = rot(tiles[b_neigh])
    # print(img)

    square += 1

for i in range(square):
    for j in range(square - 1):
        curr = img[i][j]
        _, _, _, right = tile2borders(tiles[curr])

        [r_neigh] = [x for x in get_neighs(right)  if x != curr]
        rtop, rbottom, rleft, rright = tile2borders(tiles[r_neigh])
        img[i].append(r_neigh)

        if right == rleft:
            # print('a')
            pass
        elif right == rleft[::-1]:
            # print('b')
            tiles[r_neigh] = flip_vertic(tiles[r_neigh])
        elif right == rright:
            # print('c')
            tiles[r_neigh] = flip_horiz(tiles[r_neigh])
        elif right == rright[::-1]:
            # print('d')
            tiles[r_neigh] = flip_horiz(tiles[r_neigh])
            tiles[r_neigh] = flip_vertic(tiles[r_neigh])
        elif right == rtop:
            # print('e')
            tiles[r_neigh] = rot_counter(tiles[r_neigh])
            tiles[r_neigh] = flip_vertic(tiles[r_neigh])
        elif right == rtop[::-1]:
            # print('f')
            tiles[r_neigh] = rot_counter(tiles[r_neigh])
        elif right == rbottom:
            # print('g')
            tiles[r_neigh] = rot(tiles[r_neigh])
        elif right == rbottom[::-1]:
            # print('h')
            tiles[r_neigh] = rot(tiles[r_neigh])
            tiles[r_neigh] = flip_vertic(tiles[r_neigh])

for i in range(len(img) - 1):
    for j in range(len(img) - 1):
        curr = img[i][j]
        r = img[i][j+1]
        b = img[i+1][j]
        _, bottom, _, right = tile2borders(tiles[curr])
        top, _, _, _ = tile2borders(tiles[b])
        _, _, left, _ = tile2borders(tiles[r])
        assert bottom == top, (curr, b, bottom, top)
        assert left == right


# Strip borders.
for i in range(len(img)):
    for j in range(len(img)):
        curr = img[i][j]
        tile = tiles[curr]
        tile = tile[1:-1]
        tile = [l[1:-1] for l in tile]
        tiles[curr] = tile


pic = []
for i in range(len(img)):
    for x in range(len(tile)):
        for j in range(len(img)):
            curr = img[i][j]
            tile = tiles[curr]
            pic.append(tile[x])


pic = ''.join(pic)
side = 8*square
full_pic = []
for i in range(0, len(pic), side):
    full_pic.append(pic[i:i+side])


monster = """                  #
#    ##    ##    ###
 #  #  #  #  #  #
""".splitlines()

mons_len = 20
mons_heigh = 3
mons_xy = [(x, y) for y in range(len(monster)) for x in range(len(monster[y]))  if monster[y][x] == '#']

def has_mons(window):
    for (x, y) in mons_xy:
        if window[y][x] != '#':
            return False
    return True

mons_locs = set()

attempt = 0
while len(mons_locs) == 0:
    attempt += 1
    if attempt == 5:
        full_pic = flip_horiz(full_pic)

    full_pic = rot(full_pic)

    for y in range(len(full_pic) - mons_heigh):
        for x in range(len(full_pic[y]) - mons_len):
            window = [l[x:x+mons_len] for l in full_pic[y:y+mons_heigh]]
            if has_mons(window):
                for (x_m, y_m) in mons_xy:
                    mons_locs.add((x + x_m, y+y_m))

print(pic.count('#') - len(mons_locs))
