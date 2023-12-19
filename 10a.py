import utils

DAY = 10
LEVEL = 1
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)
out = -1

m = [[y for y in x] for x in text.split('\n')]
start = ()
for i, x in enumerate(m):
    for j, y in enumerate(x):
        if y == 'S':
            start = (i, j)

q = [start]
while True:
    sz = len(q)
    if not sz:
        break
    out+=1
    for i in range(sz):
        pos = q.pop(0)
        pipe = m[pos[0]][pos[1]]
        x1 = max(0, pos[0]-1)
        y1 = max(0, pos[1]-1)
        x2 = min(pos[0]+1, len(m))
        y2 = min(pos[1]+1, len(m[0]))
        d = {'l': (pos[0], y1), 'r': (pos[0], y2), 'u': (x1, pos[1]), 'd': (x2, pos[1])}
        if pipe == 'S':
            pipe = '|'
        first = 'u'
        second = 'd'
        m[pos[0]][pos[1]] = '.'
        if pipe == '-':
            first = 'l'
            second = 'r'
        elif pipe == 'L':
            first = 'u'
            second = 'r'
        elif pipe == 'J':
            first = 'u'
            second = 'l'
        elif pipe == '7':
            first = 'l'
            second = 'd'
        elif pipe == 'F':
            first = 'r'
            second = 'd'
        if m[d[first][0]][d[first][1]] != '.':
            q.append(d[first])
        if m[d[second][0]][d[second][1]] != '.':
            q.append(d[second])




print(out)
if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)