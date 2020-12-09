f = open('./i.csv').read().split('\n')
e = []
for hj in f:
    e.append(int(hj))
preamble = []
for a in range(0,25):
    preamble.append(int(f[a]))
def func():
    for b in range(25, len(f)-1):
        summed = False
        for c in range(0,25):
            for d in range(0,25):
                if preamble[c]+preamble[d] == int(f[b]) and not preamble[c] == preamble[d] and not summed:
                    summed = True
                    preamble.append(int(f[b]))
                    del preamble[0]
                elif c == 24 and d == 24 and not summed:
                    for width in range(1,len(e)):
                        for h in range(0,len(e)-width-1):
                            li = []
                            for j in range(0,width+1):
                                li.append(e[h+j])
                            if sum(li) == int(f[b]):
                                return sorted(li)[0] + sorted(li)[len(li)-1]
print(func())