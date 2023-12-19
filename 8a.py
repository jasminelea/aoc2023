import utils

DAY = 8
LEVEL = 1
EXAMPLE = 0

input_text = utils.download(DAY, EXAMPLE)

out = 0
lines = input_text.split('\n')

d = {}
pattern = lines[0]

for l in lines[2:]:
    key, val = l.split(' = ', 1)
    left, right = val[1:-1].split(', ')
    d[key] = (left, right)

curr = 'AAA'

i = 0
while True:
    left = 0 if pattern[i] == 'L' else 1
    if curr == 'ZZZ':
        break
    curr = d[curr][left]
    i = (i + 1) % len(pattern)
    out += 1


print(out)

if not EXAMPLE:
    result = utils.submit(DAY, LEVEL, out)
