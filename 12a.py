from functools import cache

import utils

DAY = 12
LEVEL = 1
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)
out = 0
string = ""
spec = []

@cache
def solve(i, j): #answer the question if you are at index i in string and index j in spec, how many ways to solve
    if i >= len(string) or j >= len(spec):
        if '#' not in string[i:] and j == len(spec):
            return 1
        else:
            return 0

    count = 0
    if string[i] != '#':
        count += solve(i+1, j)
    if string[i] != '.':
        currLen = spec[j]
        valid = True
        # if i+currLen >= len(string):
        #     valid = False
        for c in string[i:i+currLen]:
            if c == '.':
                valid = False
        if i+currLen >= len(string) or string[i+currLen] == '#':
            valid = False
        if valid:
            count += solve(i+currLen + 1, j+1)
    return count




for line in text.splitlines():
    string, spec = line.split(' ')
    spec = [int(x) for x in spec.split(',')]
    string += '.'
    out += solve(0,0)
    solve.cache_clear()


print(out)
if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
