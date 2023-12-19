import utils

DAY = 19
LEVEL = 1
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0

workflows, ratings = text.split('\n\n')
workflows = workflows.split('\n')
ratings = ratings.split('\n')
wfs = {}
for w in workflows:
    name, rules = w.split('{')
    rules = rules[:-1].split(',')
    wfs[name] = rules
rs = [[int(x.split('=')[1]) for x in rating[1:-1].split(',')] for rating in ratings]
cats = {'x': 0, 'm': 1, 'a': 2, 's': 3}

for r in rs:
    curr = 'in'
    while True:
        rules = wfs[curr]
        next = ''
        for rule in rules:
            s = rule.split('<')
            if len(s) > 1:
                c = s[0]
                v, n = s[1].split(':')
                v = int(v)
                if r[cats[c]] < v:
                    next = n
                    break
            s = rule.split('>')
            if len(s) > 1:
                c = s[0]
                v, n = s[1].split(':')
                v = int(v)
                if r[cats[c]] > v:
                    next = n
                    break
            next = rule
            # break
        if next == 'R':
            break
        elif next == 'A':
            out += sum(r)
            # if (sum(r) == 4623 or sum(r) == 4557):
            #     print(sum(r))
            break
        curr = next
print(out)





if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
