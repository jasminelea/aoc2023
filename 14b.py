import utils

DAY = 14
LEVEL = 2
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

rows = text.split('\n')

for y in range(200):
    out = 0
    for x in range(4):
        for i, r in enumerate(rows):
            # move Os as high as possible
            for j, c in enumerate(r):
                if c != 'O':
                    continue
                poss = i
                for k in range(i-1, -1, -1):
                    if rows[k][j] == '#':
                        break
                    elif rows[k][j] == '.':
                        poss = k
                if poss != i:
                    # check if modifying enumerate modifies original rows? probably not
                    rows[i] = rows[i][:j] + '.' + rows[i][j+1:]
                    rows[poss] = rows[poss][:j] + 'O' + rows[poss][j+1:]

        #rotate rows
        nrows = []
        for i in range(len(rows[0])):
            nrows.append("")
            for j in range(len(rows)-1, -1, -1):
                nrows[-1] += rows[j][i]
        rows = nrows
    for i, r in enumerate(rows):
        for c in r:
            if c == 'O':
                out += len(rows) - i
    print(f"{y+1}: {out}")



#

# if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
