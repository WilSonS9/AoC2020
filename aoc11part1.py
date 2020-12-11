f = open('./k.csv').read().split('\n')

e = []
for a in f:
    e.append(list(a))

def func(old):
    new = []
    i = 0
    while i < len(old):
        j = 0
        row = []
        while j < len(old[0]):
            adj = 0
            for i2 in range(i-1, i+2):
                for j2 in range(j-1, j+2):
                    if 0 <= i2 < len(old) and 0 <= j2 < len(old[0]):
                        if old[i2][j2] == '#':
                            if i2 == i and j2 == j:
                                continue
                            else:
                                adj += 1
            if old[i][j] == 'L' and adj == 0:
                row.append('#')
            elif old[i][j] == '#' and adj >= 4:
                row.append('L')
            elif old[i][j] == '.':
                row.append('.')
            else:
                row.append(old[i][j])
            j += 1
        new.append(row)
        i += 1
    return((old, new))

count = 0
old = e
while True:
    myVar = func(old)
    if myVar[1] == myVar[0]:
        for hj in myVar[1]:
            count += hj.count('#')
        break
    else:
        old = myVar[1]
print(count)