f = open('./m.csv').read().split('\n')

num = int(f[0])
e = f[1].replace('x,', '').replace(',,', ',').split(',')
lowest = (10000000, 10)

for a in e:
    a = int(a)
    i = 1
    while a*i < num:
        i += 1
    if a*i < lowest[0]:
        lowest = (a*i, a)

print((lowest[0]-num) * lowest[1])