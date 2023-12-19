import utils
from functools import cmp_to_key

DAY = 7
LEVEL = 1
EXAMPLE = 1

input_text = utils.download(DAY, EXAMPLE)

weights = {
    'A': 0,
    'K': 1,
    'Q': 2,
    'J': 3,
    'T': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12,
}


def cmp(a, b):
    ans = 0
    for i in range(5):
        if ans != 0: return ans
        ans = weights[a[0][i]] - weights[b[0][i]]
    return ans


out = 0
# lines = f.readlines()
lines = input_text.split('\n')
ranks = [[] for i in range(7)]
for l in lines:
    hand, n = l.split()
    d = {}
    for c in hand:
        d[c] = d.get(c, 0) + 1
    # s = sorted(d.items(), key=lambda item: item[1])
    cards = sorted(hand, reverse=1)
    x = (hand, int(n))
    if len(d) == 1:
        ranks[6].append(x)
    elif len(d) == 2:
        if cards[0] != cards[1]:
            ranks[5].append(x)
        elif cards[3] != cards[4]:
            ranks[5].append(x)
        else:
            ranks[4].append(x)
    elif len(d) == 3:
        if 3 in d.values():
            ranks[3].append(x)
        else:
            ranks[2].append(x)
    elif len(d) == 4:
        ranks[1].append(x)
    else:
        ranks[0].append(x)
i = 1
for r in ranks:
    r.sort(key=cmp_to_key(cmp), reverse=1)
    for c in r:
        out += i * c[1]
        i += 1
print(ranks)
print(out)

if not EXAMPLE:
    utils.submit(DAY, LEVEL, out)
