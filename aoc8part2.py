f = open('./h.csv').read().split('\n')

acc = 0
e = []
iList = []
changeCount = 0

for a in f:
    e.append(a.split(' '))

i = 0
while i < len(e):
    iList.append(i)
    if e[i][0] == 'acc':
        acc += int(e[i][1])
        i += 1
    elif e[i][0] == 'jmp':
        nList = []
        n = 0
        acc2 = 0
        e[i][0] = 'nop'
        while len(nList) <= len(e) and n < len(e):
            nList.append(n)
            if e[n][0] == 'acc':
                n += 1
                acc2 += int(e[n][1])
            elif e[n][0] == 'jmp':
                n += int(e[n][1])
            elif e[n][0] == 'nop':
                n += 1
        if len(nList) <= len(e) and changeCount <= 0:
            changeCount += 1
            print(nList)
            print(acc2)
            print('Changed row', i+1, 'to nop')
            iList.pop()
        else:
            e[i][0] = 'jmp'
            i += int(e[i][1])
    elif e[i][0] == 'nop':
        jList = []
        j = 0
        acc3 = 0
        e[i][0] = 'jmp'
        while len(jList) <= len(e) and j < len(e):
            jList.append(j)
            if e[j][0] == 'acc':
                j += 1
                acc3 += int(e[j][1])
            elif e[j][0] == 'jmp':
                j += int(e[j][1])
            elif e[j][0] == 'nop':
                j += 1
        if len(jList) <= len(e) and changeCount <= 0:
            print(jList)
            changeCount += 1
            print(acc3)
            print('Changed row', i+1, 'to jmp')
            iList.pop()
        else:
            e[i][0] = 'nop'
            i += 1
print(acc)