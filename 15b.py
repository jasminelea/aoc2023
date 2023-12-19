import utils

DAY = 15
LEVEL = 2
EXAMPLE = 0

text = utils.download(DAY, EXAMPLE)

out = 0
steps = text.split(',')
dict = {}

for s in steps:
    label = s.split('=')[0]
    label = label.split('-')[0]
    if s[len(label)] == '=':
        curr = 0
        val = int(s[len(label)+1:])
        for c in label:
            curr += ord(c)
            curr *= 17
            curr %= 256
        if not curr in dict:
            dict[curr] = [(label, val)]
        else:
            index = [x for x, y in enumerate(dict[curr]) if y[0] == label]
            if len(index):
                dict[curr][index[0]] = (label, val)
            else:
                dict[curr].append((label, val))
    else:
        index = -1
        for box, lenses in dict.items():
            for i in range(len(lenses)):
                if lenses[i][0] == label:
                    index = i
                    break
            if index > -1:
                dict[box].pop(index)
                break
    # out += curr

for box, labels in dict.items():
    for i, label in enumerate(labels):
        out += (box+1) * (i+1) * label[1]
#
print(out)

if not EXAMPLE: result = utils.submit(DAY, LEVEL, out)
