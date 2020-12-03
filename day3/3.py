input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

with open('input.txt', 'r') as f:
    input = f.read()

grid = input.splitlines()
width = len(grid[0])

# Always one line down.
def slope(x_inc, y_inc):
    global grid
    x = 0
    y = 0
    tree_count = 0
    while y < len(grid):
        line = grid[y]
        pos = line[x]
        if pos == '#':
            tree_count += 1
        x = (x + x_inc) % width
        y += y_inc
    return tree_count

print(slope(3, 1))

print(slope(1, 1)
    * slope(3, 1)
    * slope(5, 1)
    * slope(7, 1)
    * slope(1, 2))
