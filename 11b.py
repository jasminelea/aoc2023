import utils

DAY = 11
LEVEL = 2
EXAMPLE = 0

out = 0
text = utils.download(DAY, EXAMPLE)

sky = [[x for x in y] for y in text.splitlines()]

ir = 0
ic = 0
gapr = [0 for x in sky]
gapc = [0 for x in sky[0]]
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
            # sky.insert(ir, ['.' for j in range(len(sky[0]))])
            # ir+=1
            gapr[ir] = 1
        ir+=1
    if ic != len(sky[0]):
        for j in range(len(sky)):
            if sky[j][ic] == '#':
                add_col = 0
                break
        if add_col:
            # for j in range(len(sky)):
            #     sky[j].insert(ic, '.')
            # ic+=1
            gapc[ic] = 1
        ic+=1

g = []
for i, x in enumerate(sky):
    for j, y in enumerate(x):
        if y == '#':
            g.append((i, j))

for i, x in enumerate(g):
    for j in range(i+1, len(g)):
        y = g[j]
        dx = abs(y[0] - x[0])
        dy = abs(y[1] - x[1])
        for k in range(min(y[0], x[0]), max(y[0], x[0])):
            if gapr[k] == 1:
                out += 999999
        for k in range(min(y[1], x[1]), max(y[1], x[1])):
            if gapc[k] == 1:
                out += 999999

        out += dx + dy

print(out)

if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
