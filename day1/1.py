with open('input.txt', 'r') as f:
    input = f.readlines()

def get_pair(nums, base):
    needs = {}
    for n in nums:
        if n in needs:
            m = base - n
            return (n, m)
        needs[(base - n)] = True
    return None


nums = list(map(lambda x: int(x), input))
base = 2020


(n, m) = get_pair(nums, base)
print("The pair is %d, %d.\n%d*%d=%d" % (n, m, n, m, n*m))

# Part 2
for n in nums:
    filtered = filter(lambda x: x != n, nums)
    res = get_pair(filtered, base - n)
    if res is not None:
        (m, l) = res
        print("The triple is %d, %d, %d\n%d*%d*%d=%d" % (n,m,l,n,m,l,n*m*l))
        exit(0)
