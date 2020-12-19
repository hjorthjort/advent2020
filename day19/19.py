with open('input.txt') as f:
    inp = f.read()


[rules, msgs] = inp.split('\n\n')
rules = rules.splitlines()
msgs = msgs.splitlines()

terms = {}
exprs = {}


def parse_rule(s):
    [n, rs] = s.split(': ')
    n = int(n)
    if rs[0] == '"':
        terms[n] = rs[1:-1]
        return
    rs = rs.split(' | ')
    rs = [[int(x) for x in r.split(' ')] for r in rs]
    exprs[n] = rs


[parse_rule(r) for r in rules]


valids = {}
def all_valids(rule_num):
    if rule_num in valids:
        return valids[rule_num]

    if rule_num in terms:
        res = set(terms[rule_num])
        valids[rule_num] = res
        return res

    def merge(set1, set2):
        for e1 in set1:
            for e2 in set2:
                yield e1 + e2

    res = set()
    for prod in exprs[rule_num]:
        vs = [all_valids(e) for e in prod]
        pres = vs[0]
        for v in vs[1:]:
            pres = merge(pres, v)

        res = res.union(pres)

    valids[rule_num] = res
    return res


v0s = all_valids(0)
print(len(list(filter(lambda m: m in v0s, msgs))))


exprs[8] = None
exprs[11] = None
del(valids[8])
del(valids[11])


def msg_match(msg, rule_num):
    if len(msg) == 0:
        return False
    if rule_num == 0:
        return any([msg_match(msg[:i], 8) and msg_match(msg[i:], 11) for i in range(1, len(msg) - 1)])
    if rule_num == 8:
        for v in all_valids(42):
            l = len(v)
            if msg == v or (msg[:l] == v and msg_match(msg[l:], rule_num)):
                return True
        return False
    if rule_num == 11:
        for v1 in all_valids(42):
            for v2 in all_valids(31):
                l1 = len(v1)
                l2 = len(v2)
                if msg == v1 + v2 or (msg[:l1] == v1 and msg[-l2:] == v2 and msg_match(msg[l1:-l2], rule_num)):
                    return True
        return False


print(len(list(filter(lambda m: msg_match(m, 0), msgs))))
