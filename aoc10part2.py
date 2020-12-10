f = open('./j.csv').read().split('\n')
e = []
for a in f:
    e.append(int(a))
e = sorted(e)
e.append(max(e) + 3)
combs = {0: 1}
for i in e:
    combs[i] = 0
    for j in range(i - 3, i):
        if j in combs:
            combs[i] += combs[j]
print(combs[max(e)])