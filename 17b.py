import utils
import heapq

DAY = 17
LEVEL = 2
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0

directions = '>v<^'
odmap = {'>': '<', 'v': '^', '<': '>', '^': 'v'}
dmap = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
grid = text.split('\n')

# (cost, x, y, direction, length of continuous)
visited = {}
curr = [(0, 0, 0, '>', 0), (0, 0, 0, 'v', 0)]

while len(curr) > 0:
    cost, x, y, direction, cont = heapq.heappop(curr)
    out = cost
    if x == len(grid) - 1 and y == len(grid[0]) - 1: break
    if visited.get((x, y, direction, cont)): continue

    visited[(x, y, direction, cont)] = 1

    for d in directions:
        if d == odmap[direction]: continue
        if cont >= 10 and d == direction: continue
        if cont < 4 and d != direction: continue
        dx, dy = dmap[d]
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]): continue

        nc = cont + 1 if d == direction else 1
        heapq.heappush(curr, (cost + int(grid[nx][ny]), nx, ny, d, nc))


print(out)


if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
