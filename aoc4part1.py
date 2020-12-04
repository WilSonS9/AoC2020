f = open('./d.csv').read().replace(' ', '\n').split('\n\n')
e = []
g = []
count = 0
for a in f:
    e += [a.replace('\\n', '\n').split('\n')]
for gn in e:
    bg = 0
    if len(gn) == 8:
        count += 1
    elif len(gn) == 7:
        for ite in gn:
            if 'cid' in ite:
                bg += 1
        if bg == 0:
            count += 1
print(count)