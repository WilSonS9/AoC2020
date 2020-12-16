f = open('./p.csv').read().split('\n\n')
i = []
j = []
validRanges = []
invalids = []
for k in f:
    j.append(k.split('\n'))
for l in j[0]:
    a = l.split(': ')
    del a[0]
    for h in a:
        b = h.split(' or ')
        for n in b:
            c = n.split('-')
            validRanges.append({'range': [*range(int(c[0]), int(c[1])+1)], 'pos': 0})
del j[2][0]
for p in j[2]:
    a = p.split(',')
    for x in a:
        trues = 0
        for h in validRanges:
            if int(x) in h['range']:
                trues += 1
        if trues < 1:
            invalids.append(int(x))
print(sum(invalids))