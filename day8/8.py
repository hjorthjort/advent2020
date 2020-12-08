from functools import reduce

with open('input.txt') as f:
    inp = f.read()

inp = [(x[0:3], int(x[4:])) for x in inp.splitlines()]

def run(inp):
    i = 0
    acc = 0
    visited = set()
    while i < len(inp):
        (instr, x) = inp[i]
        if i in visited:
            break
        visited.add(i)
        if instr == 'acc':
            acc += x
            i += 1
        if instr == 'jmp':
            i += x
        if instr == 'nop':
            i += 1

    if i >= len(inp):
        return (True, visited, acc)
    return (False, visited, acc)

(_, visited, acc) = run(inp)
print(acc)

for j in visited:
    (hyp, x) = inp[j]
    if hyp == 'acc':
        continue
    new = 'nop' if hyp == 'jmp' else 'jmp'
    new_inp = inp[0:j] + [(new, x)] + inp[j + 1:]

    (good, _, acc) = run(new_inp)
    if good:
        print(acc)
        break
