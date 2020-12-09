f = open('./i.csv').read().split('\n')
preamble = []
i2 = 25
for a in range(0,i2):
    preamble.append(int(f[a]))
def func():
    for b in range(i2, len(f)-1):
        summed = False
        for c in range(0,25):
            for d in range(0,25):
                if preamble[c]+preamble[d] == int(f[b]) and not preamble[c] == preamble[d] and not summed:
                    summed = True
                    preamble.append(int(f[b]))
                    del preamble[0]
                elif c == 24 and d == 24 and not summed:
                    return f[b]
print(func())