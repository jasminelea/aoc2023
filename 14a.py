import utils

DAY = 14
LEVEL = 1
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

rows = text.split('\n')
out = 0

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

for i, r in enumerate(rows):
    for c in r:
        if c == 'O':
            out += len(rows) - i

print(out)
#

if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
