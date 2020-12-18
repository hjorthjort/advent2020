with open('input.txt') as f:
    inp = f.read()


def parse_exp(string):
    res = []
    for c in string:
        if c != ' ':
            res.append(c)
    return res

inp = [parse_exp(l) for l in inp.splitlines()]


def find_subexp(exp):
    assert exp[-1] == ')'
    p = 0
    for i in range(len(exp)):
        c = exp[len(exp) - i - 1]
        if c == '(':
            p -= 1
        elif c == ')':
            p += 1
        if p == 0:
            return len(exp) - i - 1


def eeval(exp):
    c = exp[-1]
    if c == ')':
        close = find_subexp(exp)
        x = eeval(exp[close+1:-1])
        exp = exp[:close] + [x]
    else:
        x = int(c)
    if len(exp) == 1:
        return x
    elif exp[-2] == '+':
        return x + eeval(exp[:-2])
    elif exp[-2] == '*':
        return x * eeval(exp[:-2])


print(sum(map(eeval, inp)))

# Part 2


def eeval2(exp):
    c = exp[-1]
    if len(exp) == 1:
        return int(c)
    if exp[-1] == ')':
        close = find_subexp(exp)
        x = eeval2(exp[close+1:-1])
        return eeval2(exp[:close] + [x])
    if exp[-2] == '+':
        if exp[-3] == ')':
            close = find_subexp(exp[:-2])
        else:
            close = -3
        x = eeval2(exp[close:-2])
        return eeval2(exp[:close] + [x + int(c)])
    if exp[-2] == '*':
        return eeval2(exp[:-2]) * int(c)


print(sum(map(eeval2, inp)))
