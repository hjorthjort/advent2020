with open('input.txt') as f:
    inp = f.read()

inp = inp.splitlines()

inp = [int(x) for x in inp]

def x_in_set(x, ys):
    for j in range(len(ys)):
        for k in range(j + 1, len(ys)):
            if ys[j] + ys[k] == x:
                return True
    return False

i = 25
while i < len(inp):
    x = inp[i]
    if not x_in_set(x, inp[i-25: i]):
        weak = x
        break
    i += 1

print(weak)

j = 0
k = 2
tot = sum(inp[j:k])
while tot != weak:
    while tot > weak and j < k - 2:
        tot -= inp[j]
        j += 1
    while tot < weak and k < len(inp):
        tot += inp[k]
        k += 1

slic = inp[j:k]
print(min(slic) + max(slic))
