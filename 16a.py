import utils

DAY = 16
LEVEL = 1
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0
grid = [x for x in text.splitlines()]
curr = [(0, 0, 'r')]
split = {'r': '|', 'l': '|', 'u': '-', 'd': '-'}
energized = [["" for _ in range(len(grid[0]))] for _ in range(len(grid))]
directions = {'u': (-1, 0), 'l': (0, -1), 'd': (1, 0), 'r': (0, 1)}
backslash = {'u': 'l', 'l': 'u', 'd': 'r', 'r': 'd'}
forwardslash = {'u': 'r', 'r': 'u', 'd': 'l', 'l': 'd'}

while len(curr) > 0:
    x, y, d = curr.pop(0)
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        continue
    if d in energized[x][y]: continue
    energized[x][y] += d
    dx, dy = directions[d]
    dn = (x + dx, y + dy, d)
    d1x, d1y = directions[backslash[d]]
    d1 = (x + d1x, y + d1y, backslash[d])
    d2x, d2y = directions[forwardslash[d]]
    d2 = (x + d2x, y + d2y, forwardslash[d])
    if split[d] == grid[x][y]:
        curr.append(d1)
        curr.append(d2)
    elif grid[x][y] == '\\':
        curr.append(d1)
    elif grid[x][y] == '/':
        curr.append(d2)
    else:
        curr.append(dn)

for x in energized:
    for y in x:
        if y:
            out += 1
print(out)