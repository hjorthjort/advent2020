inp = "327465189"
moves = 100

cups = [int(x) for x in inp]

def find_next(curr, rem):
    curr = (curr - 1) % 10
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
moves = 10000000
circle = 1000000


class LList():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __eq__(self, value): return self.val == value

    def __ne__(self, value): return not self.__eq__(self, value)

    def __str__(self):
        s = ''
        curr = self
        i = 0
        while curr is not None and i < 10:
            s += str(curr.val) + ' '
            curr = curr.next
            i += 1
        appendix = '' if i < 10 else '...'
        return s + appendix

cs = [int(x) for x in inp] + list(range(10, circle + 1))
cs.reverse()

last = LList(cs[0])
cups = last

cups_reverse = { circle : last }

for c in cs[1:]:
    cups = LList(c, cups)
    cups_reverse[c] = cups

last.next = cups

for _ in range(moves):
    curr = cups
    h_1 = curr.next
    h_2 = h_1.next
    h_3 = h_2.next
    cups.next = h_3.next
    skip = [x.val for x in [h_1, h_2, h_3]]
    dest_val = ((curr.val - 2) % circle) + 1
    while dest_val in skip:
        dest_val = ((dest_val - 2) % circle) + 1
    dest = cups_reverse[dest_val]
    old_dest_neigh = dest.next
    dest.next = h_1
    h_3.next = old_dest_neigh
    cups = cups.next


neigh_1 = cups_reverse[1].next
neigh_2 = neigh_1.next
print(neigh_1.val * neigh_2.val)
