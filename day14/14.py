with open('input.txt') as f:
    inp = f.read()

inp = inp.splitlines()

mem = {}

def mask_val(m0, m1, val):
    top = (2 ** 36) - 1
    for x in m0:
        mask = top - (1 << x)
        val = val & mask
    for x in m1:
        val = val | (1 << x)
    return val

for l in inp:
    if l[:4] == 'mask':
        mask = l.split(' ')[2]
        m0 = []
        m1 = []
        for i in range(36):
            if mask[35-i] == '0':
                m0.append(i)
            elif mask[35-i] == '1':
                m1.append(i)
    elif l[:3] == 'mem':
        s = l.split(' ')
        addr = int(s[0][4:-1])
        val = int(s[2])
        mem[addr] = mask_val(m0, m1, val)

print(sum(mem.values()))

# Part 2

mem = {}


def mask_addr(mx, m1, addr):
    if mx == []:
        yield mask_val([], m1, addr)
    else:
        x = mx[0]
        top = (2 ** 36) - 1
        for addr in mask_addr(mx[1:], m1, addr):
            yield addr & (top - (1 << x))
            yield addr | (1 << x)

for l in inp:
    if l[:4] == 'mask':
        mask = l.split(' ')[2]
        mX = []
        m1 = []
        for i in range(36):
            if mask[35-i] == 'X':
                mX.append(i)
            elif mask[35-i] == '1':
                m1.append(i)
    elif l[:3] == 'mem':
        s = l.split(' ')
        addr = int(s[0][4:-1])
        val = int(s[2])
        for addr in mask_addr(mX, m1, addr):
            mem[addr] = int(s[2])

print(sum(mem.values()))
