f = open('./p.csv').read().split('\n\n')
i = []
j = []
validRanges = []
invalids = []
valids = []
for k in f:
    j.append(k.split('\n'))
for l in j[0]:
    a = l.split(': ')
    name = a[0]
    del a[0]
    for h in a:
        b = h.split(' or ')
        appender = []
        for n in b:
            c = n.split('-')
            appender.append([*range(int(c[0]), int(c[1])+1)])
        atcho = appender[0]+appender[1]
        validRanges.append({'range': atcho, 'pos': 0, 'posArr': [], 'name': name})

tick = j[1][1].split(',')

del j[2][0]
for p in j[2]:
    a = p.split(',')
    bigTrue = True
    for x in a:
        trues = 0
        for h in validRanges:
            if int(x) in h['range']:
                trues += 1
        if trues < 1:
            bigTrue = False
            invalids.append(int(x))
    if bigTrue:
        valids.append(a)

for bc in validRanges:
    for gh in range(0, len(validRanges)):
        possible = True
        for ij in range(0,len(valids)):
            if not int(valids[ij][gh]) in bc['range']:
                possible = False
                break
        if possible == True:
            bc['posArr'].append(gh)

def func():
    cont = True
    for ghj in validRanges:
        for y in ghj['posArr']:
            duplicate = False
            for hjg in validRanges:
                if y in hjg['posArr'] and not hjg == ghj:
                    duplicate = True
            if duplicate == False:
                ghj['posArr'] = [y]
                ghj['pos'] = y
                break
        if len(ghj['posArr']) > 1:
            cont = False
    if cont:
        return validRanges
    else:
        return func()

a = func()

arrr = []
arr2 = []
count = 0

for bcd in a:
    if 'departure' in bcd['name']:
        arrr.append(bcd)
for cbd in arrr:
    arr2.append(int(tick[cbd['pos']]))

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

print(product(arr2))