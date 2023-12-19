import utils

DAY = 13
LEVEL = 2
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0

def one_character_off(s1, s2):
    diff = 0
    for i, c in enumerate(s1):
        if diff > 1: break
        if c != s2[i]:
            diff += 1
    return diff == 1

def get_res(rows):
    prows = {}
    res = 0
    for i, line in enumerate(rows):
        if i == 0: continue
        for p, val in prows.items():
            idx = p - 1 - (i - p)
            if (not val) or idx < 0:
                continue
            if one_character_off(line, rows[idx]) and val[1] == 0:
                prows[p] = (1, 1)
            elif line != rows[idx]:
                prows[p] = 0

        if line == rows[i - 1]:
            prows[i] = (1, 0)
        elif one_character_off(line, rows[i - 1]):
            prows[i] = (1, 1)
    for p, v in prows.items():
        if not v or v[1] != 1: continue
        res += p
    return res

grids = text.split('\n\n')
for g in grids:
    #check rows
    rows = g.split('\n')
    # prows = {}
    # for i, line in enumerate(rows):
    #     if i == 0: continue
    #     for p, val in prows.items():
    #         idx = p-1 - (i-p)
    #         if (not val) or idx < 0:
    #             continue
    #         if one_character_off(line, rows[idx]) and val[1] == 0:
    #             prows[p] = (1, 1)
    #         elif line != rows[idx]:
    #             prows[p] = 0
    #
    #     if line == rows[i-1]:
    #         prows[i] = (1, 0)
    #     elif one_character_off(line, rows[i-1]):
    #         prows[i] = (1, 1)
    # for p, v in prows.items():
    #     if not v or v[1] != 1: continue
    #     out += p * 100
    out += get_res(rows) * 100

    #check cols
    cols = []
    for i in range(len(rows[0])):
        c = ""
        for j in range(len(rows)):
            c += rows[j][i]
        cols.append(c)
    # pcols = {}
    # for i, line in enumerate(cols):
    #     if i == 0: continue
    #     for p, val in pcols.items():
    #         idx = p - 1 - (i - p)
    #         if (not val) or idx < 0:
    #             continue
    #         if line != cols[idx]:
    #             pcols[p] = 0
    #
    #     if line == cols[i - 1]:
    #         pcols[i] = 1
    # for p, v in pcols.items():
    #     if not v: continue
    #     out += p
    out += get_res(cols)



print(out)
if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
