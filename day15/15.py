inp = [14,8,16,0,1,17]

# number and it's last turn
mem = {}

turn = 1

def step(mem, turn, next):
    if turn - 1 < len(inp):
        i = inp[turn - 1]
    else:
        i = next
    next = turn - mem[i] if i in mem else 0
    mem[i] = turn
    return next

next = -1
while turn < 2020:
    next = step(mem, turn, next)
    turn += 1

print(next)

while turn < 30000000:
    next = step(mem, turn, next)
    turn += 1

print(next)
