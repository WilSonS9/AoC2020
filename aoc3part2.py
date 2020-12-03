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
row = 1
col = 1
while row < len(f):
    # print(row)
    if list(f[row])[col] == '#':
        c2 += 1
    col += 1
    row += 1
row = 1
col = 5
while row < len(f):
    # print(row)
    if list(f[row])[col] == '#':
        c3 += 1
    col += 5
    row += 1
row = 1
col = 7
while row < len(f):
    # print(row)
    if list(f[row])[col] == '#':
        c4 += 1
    col += 7
    row += 1
row = 2
col = 1
while row < len(f):
    # print(row)
    if list(f[row])[col] == '#':
        c5 += 1
    col += 1
    row += 2

print('Count: ', c1*c2*c3*c4*c5)
