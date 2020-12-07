inp = ['FBFBBFFRLR',
       'BFFFBBFRRR',
       'FFFBBBFRRR',
       'BBFFBBFRLL']

with open('input.txt') as f:
    inp = f.read()

inp = inp.splitlines()

nums = []
for s in inp:
    n = 0
    for c in s:
        n *= 2
        if c == 'B' or c == 'R':
            n +=1
    nums.append(n)

print(max(nums))

for x in range(min(nums), max(nums)):
    if x not in nums:
        print(x)
