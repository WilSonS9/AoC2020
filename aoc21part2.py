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

allergies3 = allergies2.copy()

for j in allergies3:
    j['possibles'] = j['possibles'][0].intersection(*j['possibles'])

def identify(inp):
    old = inp.copy()
    new = old.copy()
    new2 = []
    for xyz in new:
        if len(xyz['possibles']) == 1:
            unique = list(xyz['possibles'])[0]
            for yxz in new:
                if not xyz == yxz and len(yxz['possibles']) > 1:
                    yxz['possibles'].discard(unique)
                    new2.append(yxz)
    return new2

cont = True
old = allergies3.copy()
big = []

while cont:
    hej = identify(old).copy()
    if old == hej:
        big = allergies3
        cont = False
    else:
        old = hej.copy()

big.sort(key=lambda x: x['name'])

string = ''

for abcd in big:
    string += list(abcd['possibles'])[0] + ','

print(string[0:len(string)-2])
