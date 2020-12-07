import re

f = open('./g.csv').read().split('\n')

e = []
g = []

for a in f:
    e.append(a.replace('no other bags', '').replace('.', '').split('bags contain '))
for b in e:
    if len(b[1]) > 1:
        g.append({
            'bag': b[0].replace(' ', ''),
            'contains': re.sub('s$', '', re.sub('s,', ',', b[1].replace(' bag', '').replace(' bags', '').replace(' ', ''))).split(',')
        })
    else:
        g.append({
            'bag': b[0].replace(' ', ''),
            'contains': []
        })
def search(dic):
    d = 0
    for bg in dic['contains']:
        try:
            d += int(bg[0])
            h = list(filter(lambda t: t['bag'] == bg[1:], g))
            c = search(h[0])
            d += int(c) * int(bg[0])
        except:
            return 0
    return d
hj = search(list(filter(lambda h: h['bag'] == 'shinygold', g))[0])
print(hj)