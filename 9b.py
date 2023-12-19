import utils

DAY = 9
LEVEL = 2
EXAMPLE = 0

input_text = utils.download(DAY, EXAMPLE)

out = 0
lines = input_text.split('\n')
sequences = []

def find_increase(arr):
    prev = arr[0]
    new = []
    call_next = 0
    for a in arr[1:]:
        new.append(a-prev)
        if a-prev:
            call_next = 1
        prev = a
    if call_next:
        return arr[0] - find_increase(new)
    else:
        return arr[0]


for l in lines:
    sequences.append([int(x) for x in l.split()])

for s in sequences:
    out+=find_increase(s)


print(out)

if not EXAMPLE:
    result = utils.submit(DAY, LEVEL, out)
