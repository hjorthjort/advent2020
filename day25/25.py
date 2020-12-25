import math
door_pub = 8335663
card_pub = 8614349

N = 20201227
m = math.ceil(math.sqrt(N))

def pow(a, b):
    """Fast exponentiation algorithm in the prime field for `N`.
    returns a^b mod N
    """
    if b == 0:
        return 1
    rem = pow(a**2 % N, b // 2)
    if b % 2 == 1:
        return (a * rem) % N
    return rem % N

js = [1]
for _ in range(m):
    js.append((js[-1] * 7) % N)

am = pow(pow(7, N-2), m)

def brute_secret(pub):
    y = pub
    for i in range(m):
        for j in range(m+1):
            if y == js[j]:
                return i * m + j
        y = (y * am) % N

door_loop = brute_secret(door_pub)

print(pow(card_pub, door_loop))
