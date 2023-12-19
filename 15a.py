import utils

DAY = 15
LEVEL = 1
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0
steps = text.split(',')

for s in steps:
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    out += curr

#
print(out)

if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
