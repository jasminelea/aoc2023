import utils

DAY = 11
LEVEL = 1
EXAMPLE = 0

out = 0
text = utils.download(DAY, EXAMPLE)

sky = [[x for x in y] for y in text.splitlines()]

ir = 0
ic = 0
while True:
    if ir == len(sky) and ic == len(sky[0]):
        break
    add_row = 1
    add_col = 1
    if ir != len(sky):
        for j in range(len(sky[0])):
            if sky[ir][j] == '#':
                add_row = 0
                break
        if add_row:
            sky.insert(ir, ['.' for j in range(len(sky[0]))])
            ir+=1
        ir+=1
    if ic != len(sky[0]):
        for j in range(len(sky)):
            if sky[j][ic] == '#':
                add_col = 0
                break
        if add_col:
            for j in range(len(sky)):
                sky[j].insert(ic, '.')
            ic+=1
        ic+=1

g = []
for i, x in enumerate(sky):
    for j, y in enumerate(x):
        if y == '#':
            g.append((i, j))

for i, x in enumerate(g):
    for j in range(i+1, len(g)):
        y = g[j]
        out += abs(y[0] - x[0])
        out += abs(y[1] - x[1])

print(out)

if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
