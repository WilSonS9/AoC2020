f = open('./v.csv').read().split('\n')

e = []
wordList = []
notPossibles = []
allergies = []

for a in f:
    a = a.split(' (')
    contains = a[1].replace(')', '').replace('contains ', '').split(', ')
    foreigns = a[0].split(' ')
    for d in contains:
        allergies.append({'name': d, 'possibles': []})
    for b in foreigns:
        wordList.append(b)
    e.append({'foreigns': foreigns, 'contains': contains})

allergies2 = []
for x in allergies:
    count = 0
    for y in allergies2:
        if y['name'] == x['name']:
            count += 1
    if count == 0:
        allergies2.append(x)

for ghj in allergies2:
    for ab in e:
        if ghj['name'] in ab['contains']:
            ghj['possibles'].append(set(ab['foreigns']))

allergies3 = allergies2

for j in allergies3:
    j['possibles'] = j['possibles'][0].intersection(*j['possibles'])

for xy in wordList:
    count = 0
    for z in allergies3:
        if xy in z['possibles']:
            count += 1
    if count == 0:
        notPossibles.append(xy)

count2 = 0
notPossibles = set(notPossibles)
for abc in notPossibles:
    for xyz in e:
        if abc in xyz['foreigns']:
            count2 += 1

print(count2)