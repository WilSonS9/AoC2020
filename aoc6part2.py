f = open('./f.csv').read().split('\n\n')

e = []
count = 0

for a in f:
    e.append(a.split('\n'))
for g in e:
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if "".join(g).count(ch) >= len(g):
            count += 1

print(count)