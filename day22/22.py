with open('input.txt', 'r') as f:
    inp = f.read()


inp = inp.split('\n\n')


[p1, p2] = [ [int(c) for c in p.splitlines()[1:]] for p in inp]

def round(d1, d2):
    c1, c2 = d1[0], d2[0]
    d1, d2 = d1[1:], d2[1:]
    if c1 > c2:
        return d1 + [c1, c2], d2
    return d1, d2 + [c2, c1]

def game(d1, d2):
    while len(d1) > 0 and len(d2) > 0:
        d1, d2 = round(d1, d2)
    return d1, d2

def score(p1, p2):
    res = []
    d = p1 + p2
    for i in range(len(d)):
        res.append(d.pop() * (i+1))
    return sum(res)

d1, d2 = p1.copy(), p2.copy()
d1, d2 = game(d1, d2)
print(score(d1, d2))

# Part 2

rounds = 0
def game(d1, d2):
    global rounds
    rounds += 1
    seen = []
    while len(d1) > 0 and len(d2) > 0:
        if (d1, d2) in seen:  # Inf recursion coming up.
            return (d1 + d2, [])
        seen.append((d1, d2))
        c1, c2 = d1[0], d2[0]
        d1, d2 = d1[1:], d2[1:]
        if c1 <= len(d1) and c2 <= len(d2):
            # Play sub-game.
            (x, y) = game(d1[:c1], d2[:c2])
            if len(y) == 0:  # Player 1 won sub-game.
                d1 = d1 + [c1, c2]
            else:
                d2 = d2 + [c2, c1]
        # No sub-game
        else:
            if c1 > c2:
                d1 = d1 + [c1, c2]
            else:
                d2 = d2 + [c2, c1]
    return d1, d2

d1, d2 = p1.copy(), p2.copy()
d1, d2 = game(d1, d2)

print(score(d1, d2))

print(rounds)
