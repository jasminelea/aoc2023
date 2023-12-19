from functools import cache

import utils

DAY = 12
LEVEL = 2
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)
out = 0

@cache
def solve(i, j): #answer the question if you are at index i in string and index j in spec, how many ways to solve
    if i >= len(string) or j >= len(spec):
        return 1 if '#' not in string[i:] and j == len(spec) else 0

    count = 0
    if string[i] != '#':
        count += solve(i+1, j)
    if string[i] != '.':
        if '.' in string[i:i+spec[j]] or i+spec[j] >= len(string) or string[i+spec[j]] == '#':
            return count
        count += solve(i+spec[j] + 1, j+1)
    return count


for line in text.splitlines():
    string, spec = line.split(' ')
    spec = [int(x) for x in spec.split(',')]
    string = (string + '?') * 5
    string = string[:-1] + '.'
    spec *= 5
    out += solve(0,0)
    solve.cache_clear()


print(out)
# if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
