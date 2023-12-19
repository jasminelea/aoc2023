import utils
from math import prod

DAY = 19
LEVEL = 2
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0

workflows, _ = text.split('\n\n')
workflows = workflows.split('\n')
wfs = {}
for w in workflows:
    name, rules = w.split('{')
    rules = rules[:-1].split(',')
    wfs[name] = rules
cats = {'x': 0, 'm': 1, 'a': 2, 's': 3}


def get_outcome(curr, trange):
    if curr == 'R':
        return 0
    elif curr == 'A':
        result = prod([abs(x[1] - x[0])+1 for x in trange])
        return result
    rules = wfs[curr]
    result = 0
    for rule in rules:
        s = rule.split('<')
        single = True
        if len(s) > 1:
            single = False
            c = s[0]
            v, n = s[1].split(':')
            v = int(v)
            nrange = trange.copy()
            nrange[cats[c]] = (nrange[cats[c]][0], v-1)
            trange[cats[c]] = (v, trange[cats[c]][1])
            result += get_outcome(n, nrange)

        s = rule.split('>')
        if len(s) > 1:
            single = False
            c = s[0]
            v, n = s[1].split(':')
            v = int(v)
            nrange = trange.copy()
            nrange[cats[c]] = (v+1, nrange[cats[c]][1])
            trange[cats[c]] = (trange[cats[c]][0], v)
            result += get_outcome(n, nrange)

        if single:
            result += get_outcome(rule, trange)
    return result

out = get_outcome('in', [(1, 4000), (1, 4000), (1, 4000), (1, 4000)])

print(out)





if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
