input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

with open('input.txt') as f:
    input = f.read()
    pass

lines = input.splitlines()

def is_valid(min, max, letter, password):
    occurs = len(list(filter(lambda x: x == letter, password)))
    return min <= occurs <= max

def line_is_valid(line, checker=is_valid):
    [range_raw, letter_raw, password] = line.split(' ')
    [min_raw, max_raw] = range_raw.split('-')
    min = int(min_raw)
    max = int(max_raw)
    letter = letter_raw[0]
    assert min < max
    return checker(min, max, letter, password)

print("1: %d" % len(list(filter(line_is_valid, lines))))

def is_new_valid(first, second, letter, password):
    first  -= 1
    second -= 1
    return (password[first] == letter) != (password[second] == letter)

print("2: %d" % len(list(filter(lambda l: line_is_valid(l, checker=is_new_valid), lines))))
