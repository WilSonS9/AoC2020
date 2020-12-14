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

for h in range(100001):
    mem.append(0)

for c in e:
    mask = ''
    for d in c:
        if 'mask' in d[0]:
            mask = d[1]
        elif 'mem' in d[0]:
            num = str(bin(int(d[1]))).replace('0b', '')
            num = re.sub('^', (len(mask)-len(num))*'0', num)
            i = 0
            new = ''
            while i<len(mask):
                if not mask[i] == 'X':
                    new += mask[i]
                else:
                    new += num[i]
                i += 1
            ind = re.search(r"\[([A-Za-z0-9_]+)\]", d[0]).group(1)
            mem[int(ind)] = int(new, 2)

print(sum(mem))