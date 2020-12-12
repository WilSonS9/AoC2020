f = open('./l.csv').read().split('\n')

e = []

for a in f:
    e.append([a[0:1], int(a[1:])])

dirList = ['E', 'S', 'W', 'N']
currentDir = 'E'
East = 0
West = 0
North = 0
South = 0

for g in e:
    if g[0] == 'F':
        g[0] = currentDir
    if g[0] == 'E':
        East += g[1]
    elif g[0] == 'W':
        West += g[1]
    elif g[0] == 'N':
        North += g[1]
    elif g[0] == 'S':
        South += g[1]
    elif g[0] == 'R':
        c1 = 0
        i = dirList.index(currentDir)
        while c1 < g[1]/90:
            if 0<=i+1<len(dirList):
                i += 1
                c1 += 1
            elif i+1>=len(dirList):
                i -= len(dirList)
        currentDir = dirList[i]
    elif g[0] == 'L':
        c2 = 0
        j = dirList.index(currentDir)
        while c2 < g[1]/90:
            if 0<=j-1<len(dirList):
                j -= 1
                c2 += 1
            elif j-1<0:
                j += len(dirList)
        currentDir = dirList[j]

print(abs(East-West) + abs(North-South))