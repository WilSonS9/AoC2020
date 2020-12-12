f = open('./l.csv').read().split('\n')

e = []

for a in f:
    e.append([a[0:1], int(a[1:])])

East = 0
West = 0
North = 0
South = 0

East2= 10
West2= 0
North2 = 1
South2 = 0

for g in e:
    if g[0] == 'E':
        East2 += g[1]
    elif g[0] == 'W':
        West2 += g[1]
    elif g[0] == 'N':
        North2 += g[1]
    elif g[0] == 'S':
        South2 += g[1]
    elif g[0] == 'F':
        East += East2*g[1]
        West += West2*g[1]
        North += North2*g[1]
        South += South2*g[1]
    elif g[0] == 'R':
        c1 = 0
        while c1 < g[1]/90:
            East2, South2, West2, North2 = North2, East2, South2, West2
            c1 += 1
    elif g[0] == 'L':
        c2 = 0
        while c2 < g[1]/90:
            East2, South2, West2, North2 = South2, West2, North2, East2
            c2 += 1

print(abs(East-West) + abs(North-South))