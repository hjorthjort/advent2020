inp = "327465189"
moves = 100

cups = [int(x) for x in inp]

def find_next(curr, rem):
    curr = (curr - 1) % (len(rem) + 1)
    if curr in rem:
        return rem.index(curr)
    return find_next(curr, rem)

def play(cups, moves):
    l = len(cups)
    for i in range(moves):
        curr = cups[0]
        hold = cups[1:4]
        rem = cups[4:]
        dest = find_next(curr, rem)
        cups = rem[:dest+1] + hold + rem[dest+1:] + [curr]
        assert len(cups) == l
    return cups

cups = play(cups, moves)
i = cups.index(1)
print(''.join(map(str, cups[i+1:] + cups[:i])))

# Part 2
inp = "389125467"

cups = [int(x) for x in inp]
m = max(cups)
moves = 100

cups = { i : cups[i] for i in range(len(cups))}
cups_rev = { cups[i] : i for i in range(len(cups))}

def update_cups(cup, idx):
    cups[idx] = cup
    cups_rev[cup] = idx

for i in range(10, 10):
    cups[i] = i
    cups_rev[i] = i

def find_next(curr, cups, skips, length):
    curr = (curr - 1) % length
    if curr in cups_rev and curr not in skips:
        return cups[curr]
    return find_next(curr, cups, skips, length)

def play(cups, moves):
    l = len(cups)
    for i in range(moves):
        i = i % l + 1
        print([cups[i] for i in range(len(cups))])
        print(cups_rev)
        print(i)
        assert cups_rev[cups[i]] == i
        curr = cups[i]
        holds = [cups[(i+j) % l] for j in range(1, 4)]
        dest = find_next(curr, cups, holds, l)

        upds = []
        if i < dest:
            for j in range(i + 4, dest + 1):
                upds.append((cups_rev[cups[j]], cups[j] - 3))
        else:
            for j in range(dest + 1, i + 1):
                upds.append(([cups_rev[cups[j]]], cups[j] + 3))

        upds.append((holds[0], dest + 1))
        upds.append((holds[1], dest + 2))
        upds.append((holds[2], dest + 3))
        print(upds)

        for (k, v) in upds:
            update_cups(k, v)



play(cups, moves)
print(cups)
one_idx = cups_rev[1]
print(cups[one_idx+1] * cups[one_idx + 2])
