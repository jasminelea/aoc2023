import utils
import math

DAY = 8
LEVEL = 2
EXAMPLE = 0

input_text = utils.download(DAY, EXAMPLE)

out = 1
lines = input_text.split('\n')

d = {}
pattern = lines[0]
a = []
z = []

for l in lines[2:]:
    key, val = l.split(' = ', 1)
    left, right = val[1:-1].split(', ')
    d[key] = (left, right)
    if key[2] == 'A':
        a.append(key)
    elif key[2] == 'Z':
        z.append(key)

# curr = 'AAA'

i = 0
count = 0
while True:
    left = 0 if pattern[i] == 'L' else 1
    c = []
    count += 1
    if len(a) == 0:
        break;
    for s in a:
        if d[s][left] not in z:
            c.append(d[s][left])
        else:
            out = math.lcm(out, count)

    a = c
    i = (i + 1) % len(pattern)


print(out)

if not EXAMPLE:
    result = utils.submit(DAY, LEVEL, out)
