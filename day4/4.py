input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

with open('input.txt', 'r') as f:
    input = f.read()[:-1]  # Skip final newline.

raw = [s.replace('\n', ' ') for s in input.split('\n\n')]

pre_passes = [s.split(' ') for s in raw]

required = ["byr" , "iyr" , "eyr" , "hgt" , "hcl" , "ecl" , "pid"]

count = 0

passes = []
for p in pre_passes:
    new = [f.split(':', 1) for f in p]
    passes.append(dict(new))

def has_required(fields):
    for r in required:
        if r not in fields:
            return False
    return True

req_valid = [ p for p in passes if has_required(p.keys()) ]

print(len(req_valid))

def is_year(n, min, max):
    return is_num(n, min, max, 4)

def is_num(n, min, max, nlen):
    if not (len(n) == nlen and n.isdigit()):
        return False
    x = int(n)
    if min > x or max < x:
        return False
    return True

def is_valid(p):
    if not has_required(p.keys()):
        return False
    #byr
    if not is_year(p['byr'], 1920, 2002):
        return False
    #iyr
    if not is_year(p['iyr'], 2010, 2020):
        return False
    #eyr
    if not is_year(p['eyr'], 2020, 2030):
        return False
    #hgt
    hgt = p['hgt']
    unit = hgt[-2:]
    val = hgt[:-2]
    if not (unit == 'cm' or unit == 'in'):
        return False
    if unit == 'cm' and not is_num(val, 150, 193, 3):
        return False
    if unit == 'in' and not is_num(val, 59, 76, 2):
        return False
    #hcl
    hcl = p['hcl']
    if not hcl[0] == '#':
        return False
    try:
        int(hcl[1:], 16)
    except ValueError:
        return False
    #ecl
    if p['ecl'] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    #pid
    if not is_num(p['pid'], 0, 999999999, 9):
        return False
    return True

valid = [p for p in passes if is_valid(p)]
print(len(valid))
