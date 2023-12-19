import utils

DAY = 13
LEVEL = 1
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0
grids = text.split('\n\n')
for g in grids:
    #check rows
    rows = g.split('\n')
    prows = {}
    for i, line in enumerate(rows):
        if i == 0: continue
        for p, val in prows.items():
            idx = p-1 - (i-p)
            if (not val) or idx < 0:
                continue
            if line != rows[idx]:
                prows[p] = 0

        if line == rows[i-1]:
            prows[i] = 1
    for p, v in prows.items():
        if not v: continue
        out += p * 100
    cols = []
    for i in range(len(rows[0])):
        c = ""
        for j in range(len(rows)):
            c += rows[j][i]
        cols.append(c)
    pcols = {}
    for i, line in enumerate(cols):
        if i == 0: continue
        for p, val in pcols.items():
            idx = p - 1 - (i - p)
            if (not val) or idx < 0:
                continue
            if line != cols[idx]:
                pcols[p] = 0

        if line == cols[i - 1]:
            pcols[i] = 1
    for p, v in pcols.items():
        if not v: continue
        out += p



print(out)
if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
