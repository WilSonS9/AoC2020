f = open('./q.csv').read().split('\n')

e = {}
y = 0
while y < len(f):
    x = 0
    while x < len(f[0]):
        z = 0
        w = 0
        string = str(x) + ',' + str(y) + ',' + str(z) + ',' + str(w)
        e[string] = {}
        e[string]['name'] = string
        e[string]['coords'] = [x, y, z, w]
        if f[y][x] == '#':
            e[string]['active'] = True
        else:
            e[string]['active'] = False
        x += 1
    y += 1

def expand(inp):
    new = {}
    for point in inp:
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        if not [x, y, z, w] == inp[point]['coords']:
                            x2 = inp[point]['coords'][0] + x
                            y2 = inp[point]['coords'][1] + y
                            z2 = inp[point]['coords'][2] + z
                            w2 = inp[point]['coords'][3] + w
                            string2 = str(x2) + ',' + str(y2) + ',' + str(z2) + ',' + str(w2)
                            try:
                                if inp[string2]['active'] == True or inp[string2]['active'] == False:
                                    new[string2] = inp[string2]
                                    continue
                            except:
                                new[string2] = {}
                                new[string2]['coords'] = [x2, y2, z2, w2]
                                new[string2]['active'] = False
                                new[string2]['name'] = string2
    return new    

def func(old):
    new = {}
    for point in old:
        adj = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        x2 = old[point]['coords'][0] + x
                        y2 = old[point]['coords'][1] + y
                        z2 = old[point]['coords'][2] + z
                        w2 = old[point]['coords'][3] + w
                        string2 = str(x2) + ',' + str(y2) + ',' + str(z2) + ',' + str(w2)
                        if not [x2, y2, z2, w2] == old[point]['coords']:
                            try:
                                if old[string2]['active'] == True:
                                    adj += 1
                            except:
                                pass
        newDict = {}
        if old[point]['active'] == False and adj == 3:
            newDict['active'] = True
        elif old[point]['active'] == True:
            if adj == 2 or adj == 3:
                newDict['active'] = True
            else:
                newDict['active'] = False
        else:
            newDict['active'] = old[point]['active']
        newDict['coords'] = old[point]['coords']
        newDict['name'] = old[point]['name']
        new[newDict['name']] = newDict
    return new

a = func(expand(func(expand(func(expand(func(expand(func(expand(func(expand(e))))))))))))

count = 0
for ghj in a:
    if a[ghj]['active'] == True:
        count += 1

print(count)