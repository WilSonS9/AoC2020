f = open('../b.csv').read()
d = f.split('\n')
e = []
b = []
i = 0
numValid = 0
num2 = 0
for ite in d:
    e+=ite.split('-')
for a in e:
    b+=a.split(' ')
while i<len(b):
    c2 = 0
    ar = []
    for ch in b[i+3]:
        ar.append(ch)
    if ar[int(b[i])-1] == b[i+2][0:1]:
        c2 += 1
    if ar[int(b[i+1])-1] == b[i+2][0:1]:
        c2 += 1
    if c2 == 1:
        numValid += 1
    else:
        num2 += 1
    i += 4
print(num2)
print(numValid)