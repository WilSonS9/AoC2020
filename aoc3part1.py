f = open('./c.csv').read().split('\n')
row = 1
col = 3
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
i = 0
while i< len(f):
    f[i] += 500*f[i]
    i += 1
while row < len(f):
    # print(row)
    if list(f[row])[col] == '#':
        c1 += 1
    col += 3
    row += 1

print(c1)