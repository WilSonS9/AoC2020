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
            'contains': re.sub('s$', '', re.sub('s,', ',', re.sub(r'\d', '', b[1].replace(' bag', '').replace(' bags', '').replace(' ', '')))).split(',')
        })
    else:
        g.append({
            'bag': b[0].replace(' ', ''),
            'contains': []
        })
def look(di):
    for bag in di['contains']:
        if bag == 'shinygold':
            return True
        else:
            h = list(filter(lambda b: b['bag'] == bag, g))
            if look(h[0]):
                return True
i = 0
count = 0
while i<len(g):
    if look(g[i]):
        count += 1
    i += 1
print(count)