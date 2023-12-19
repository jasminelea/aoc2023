import utils

DAY = 18
LEVEL = 2
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)
out = 0

points = []
x = 0
y = 0
edge = 0
d = "RDLU"
for line in text.splitlines():
    _, _, colour = line.split(' ')
    length = colour[2:-2]
    direction = d[int(colour[-2])]
    length = int(length, 16)
    if direction == 'D':
        x += length
    elif direction == 'U':
        x -= length
    elif direction == 'L':
        y -= length
    elif direction == 'R':
        y += length

    # px, py = points[-1]
    points.append((x, y))
    edge += length

for i in range(len(points)):
    out += points[i][1] * (points[(i-1) % len(points)][0] - points[(i+1) % len(points)][0])

out = abs(out)
out //= 2

i = out - (edge // 2) + 1
out = i + edge

print(out)



if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
