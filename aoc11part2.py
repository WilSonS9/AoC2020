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
            c1 = 0
            c2 = 0
            c3 = 0
            c4 = 0
            c5 = 0
            c6 = 0
            c7 = 0
            c8 = 0
            for bg in range(1, len(old)):
                if 0 <= i+bg < len(old) and c1 == 0:
                    if not old[i+bg][j] == '.':
                        c1 += 1
                        if old[i+bg][j] == '#':
                            adj += 1
                if 0 <= i-bg < len(old) and c2 == 0:
                    if not old[i-bg][j] == '.':
                        c2 += 1
                        if old[i-bg][j] == '#':
                            adj += 1
                if 0 <= j+bg < len(old[0]) and c3 == 0:
                    if not old[i][j+bg] == '.':
                        c3 += 1
                        if old[i][j+bg] == '#':
                            adj += 1
                if 0 <= j-bg < len(old[0]) and c4 == 0:
                    if not old[i][j-bg] == '.':
                        c4 += 1
                        if old[i][j-bg] == '#':
                            adj += 1
                if 0 <= j+bg < len(old[0]) and 0 <= i+bg < len(old) and c5 == 0:
                    if not old[i+bg][j+bg] == '.':
                        c5 += 1
                        if old[i+bg][j+bg] == '#':
                            adj += 1
                if 0 <= j-bg < len(old[0]) and 0 <= i+bg < len(old) and c6 == 0:
                    if not old[i+bg][j-bg] == '.':
                        c6 += 1
                        if old[i+bg][j-bg] == '#':
                            adj += 1
                if 0 <= j+bg < len(old[0]) and 0 <= i-bg < len(old) and c7 == 0:
                    if not old[i-bg][j+bg] == '.':
                        c7 += 1
                        if old[i-bg][j+bg] == '#':
                            adj += 1
                if 0 <= j-bg < len(old[0]) and 0 <= i-bg < len(old) and c8 == 0:
                    if not old[i-bg][j-bg] == '.':
                        c8 += 1
                        if old[i-bg][j-bg] == '#':
                            adj += 1
            if old[i][j] == 'L' and adj == 0:
                row.append('#')
            elif old[i][j] == '#' and adj >= 5:
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
while True: # Might take a solid 5 minutes to complete :)
    myVar = func(old)
    if myVar[1] == myVar[0]:
        for hj in myVar[1]:
            count += hj.count('#')
        break
    else:
        old = myVar[1]
print(count)