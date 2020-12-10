f = open('./j.csv').read().split('\n')
e = []
current = 0
dif1 = 0
dif3 = 1
for a in f:
    e.append(int(a))
e = sorted(e)
for b in e:
    if b-current == 1:
        dif1 += 1
    elif b-current == 3:
        dif3 += 1
    current = b
print(dif1*dif3)