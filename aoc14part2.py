import re

f = open('./n.csv').read()
g = f.replace('mask', '\nmask').split('\n\n')

j = []
e = []

for a in g:
    j.append(a.split('\n'))

for bc in j:
    li = []
    for gh in bc:
        li.append(gh.split(' = '))
    e.append(li)

del e[0][0]

mem = []

mem = {}

def combMaker(s):
    combs = []
    j = 0
    while j < len(s):
        if s[j] == 'X':
            aha = list(s)
            aha[j] = '0'
            if not 'X' in ''.join(aha):
                combs.append(''.join(aha))
                aha[j] = '1'
                combs.append(''.join(aha))
                return combs
            else:
                var1 = combMaker(''.join(aha))
                for hj in var1:
                    gh = list(hj)
                    gh[j] = '0'
                    combs.append(''.join(gh))
                    gh[j] = '1'
                    combs.append(''.join(gh))
                return(combs)
        j += 1

for c in e:
    mask = ''
    for d in c:
        if 'mask' in d[0]:
            mask = d[1]
        elif 'mem' in d[0]:
            num = int(d[1])
            ind = str(bin(int(re.search(r"\[([A-Za-z0-9_]+)\]", d[0]).group(1)))).replace('0b', '')
            ind = re.sub('^', (len(mask)-len(ind))*'0', ind)
            new = ''
            i = 0
            while i < len(mask):
                if mask[i] == '0':
                    new += ind[i]
                else:
                    new += mask[i]
                i += 1
            var = combMaker(new)
            for ijk in var:
                mem[int(ijk, 2)] = num
count = 0
for gkjirk in mem:
    count += mem[gkjirk]
print(count)