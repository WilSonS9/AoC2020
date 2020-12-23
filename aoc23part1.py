f = list(open('x.csv').read())

e = []

for a in f:
    e.append(int(a))


def game(end):
    newLi = e.copy()
    count2 = 0
    i2 = 0
    while count2 < end:
        result = doRound(i2, newLi)
        newLi = result[1].copy()
        i2 = result[0]
        count2 += 1

    return newLi

def doRound(i, li):
    n = li[i]
    throwAway = []
    c = 1
    while c < 4:
        throwAway.append(li[(i+c) % len(li)])
        c += 1
    for d in throwAway:
        li.remove(d)
    destination = 0
    cont = True
    j = -1
    i = li.index(n)
    while cont:
        i3 = i % len(li)
        if li[i3]+j in li:
            destination = li.index(li[i3]+j)
            cont = False
        elif li[i3]+j < min(li):
            j = max(li)-li[i3]
        else:
            j -= 1
    for b in reversed(throwAway):
        li.insert(destination+1, b)
    i = li.index(n)
    newI = (i+1) % len(li)

    return (newI, li)

def makeString(lis):
    s = ''
    c3 = 1
    i = lis.index(1)+1
    while c3 < len(lis):
        i = i % len(lis)
        s += str(lis[i])
        i += 1
        c3 += 1
    return s

print(makeString(game(100)))