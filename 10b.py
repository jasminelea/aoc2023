import utils

DAY=10
LEVEL=2
EXAMPLE=0

text=utils.download(DAY, EXAMPLE)
out=0

ma=[[y for y in x] for x in text.split('\n')]
start=()
for i, x in enumerate(ma):
    for j, y in enumerate(x):
        if y=='S':
            start=(i, j)
            ma[i][j]='|' if not EXAMPLE else '7'

m=[[y for y in x] for x in ma]
q=[start]
while True:
    sz=len(q)
    if not sz:
        break
    for i in range(sz):
        pos=q.pop(0)
        pipe=m[pos[0]][pos[1]]
        if pipe=='*':
            continue
        d={'l': (pos[0], pos[1]-1), 'r': (pos[0], pos[1]+1), 'u': (pos[0]-1, pos[1]), 'd': (pos[0]+1, pos[1])}
        p={'|': ('u', 'd'), '-': ('l','r'), 'L': ('u','r'), 'J': ('u','l'), '7': ('l','d'), 'F': ('r','d')}

        nex=d[p[pipe][0]]
        m[pos[0]][pos[1]]='*'
        if m[nex[0]][nex[1]]!='.' and m[nex[0]][nex[1]]!='*':
            q.append(nex)
        nex=d[p[pipe][1]]
        if m[nex[0]][nex[1]]!='.' and m[nex[0]][nex[1]]!='*':
            q.append(nex)

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j]=='*':
            continue
        bef=0
        prev=0
        for k in range(i):
            if m[k][j]!='*':
                continue
            pipe=ma[k][j]
            if pipe=='-':
                bef+=1
            elif pipe=='L' or pipe=='F':
                prev-=1
                if prev==0:
                    bef+=1
                elif not prev % 2:
                    prev=0
            elif pipe=='7' or pipe=='J':
                prev+=1
                if prev==0:
                    bef+=1
                elif not prev % 2:
                    prev=0
        if not bef % 2:
            continue
        bef=0
        for k in range(j):
            if m[i][k]!='*':
                continue
            pipe=ma[i][k]
            if pipe=='|':
                bef+=1
            elif pipe=='L' or pipe=='J':
                prev-=1
                if prev==0:
                    bef+=1
                elif not prev % 2:
                    prev=0
            elif pipe=='7' or pipe=='F':
                prev+=1
                if prev==0:
                    bef+=1
                elif not prev % 2:
                    prev=0
        if not bef % 2:
            continue
        out+=1


print(out)
# if not EXAMPLE: result=utils.submit(DAY, LEVEL, out)