import utils

DAY = 16
LEVEL = 2
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0
grid = [x for x in text.splitlines()]
split = {'r': '|', 'l': '|', 'u': '-', 'd': '-'}
directions = {'u': (-1, 0), 'l': (0, -1), 'd': (1, 0), 'r': (0, 1)}
backslash = {'u': 'l', 'l': 'u', 'd': 'r', 'r': 'd'}
forwardslash = {'u': 'r', 'r': 'u', 'd': 'l', 'l': 'd'}

for i in range(len(grid[0]) -1):
    for j in [0, len(grid) - 1]:
        curr = [(j, i, 'd' if j == 0 else 'u')]
        energized = [["" for _ in range(len(grid[0]))] for _ in range(len(grid))]

        temp = 0
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
                    temp += 1
        out = max(out, temp)
print(out)


if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)