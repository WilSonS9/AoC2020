from collections import OrderedDict

f = open('./f.csv').read().split('\n\n')

e = []
strList = []
count = 0

for a in f:
    e.append(a.split('\n'))
for g in e:
    strList.append("".join(OrderedDict.fromkeys("".join(g))))
for j in strList:
    count += len(j)

print(count)