from re import findall

f = open('y.csv').read().split('\n')

tiles = {}

def do(coords, move):
    x = int(coords[1])
    y = int(coords[0])
    if move == 'e':
        x += 2
    elif move == 'w':
        x -= 2
    elif move == 'ne':
        y += 2
        x += 1
    elif move == 'nw':
        y += 2
        x -= 1
    elif move == 'se':
        y -= 2
        x += 1
    elif move == 'sw':
        y -= 2
        x -= 1
    return (str(y), str(x))

for command in f:
    coords = ('0', '0')
    commands = findall('e|w|se|sw|ne|nw', command)
    for doin in commands:
        coords = do(coords, doin)
    s = ' '.join(coords)
    tDict = {'adj': []}
    if s in tiles:
        tDict['black'] = not tiles[s]
    else:
        tDict['black'] = True
    tiles[s] = tDict

def expand(dictionary):
    new = {}
    for hui in dictionary:
        name = hui.split(' ')
        x = int(name[1])
        y = int(name[0])
        adjes = [' '.join([str(y+2), str(x+1)]), ' '.join([str(y+2), str(x-1)]), ' '.join([str(y), str(x+2)]), ' '.join([str(y), str(x-2)]), ' '.join([str(y-2), str(x+1)]), ' '.join([str(y-2), str(x-1)]), ' '.join([str(y), str(x)])]
        for abc in adjes:
            if not abc in dictionary:
                new[abc] = {'black': False}
            else:
                new[abc] = dictionary[abc]
    return new

def simulateDay(dic):
    dic = expand(dic).copy()
    newD = {}
    for tile in dic:
        newT = {}
        c2 = 0
        name = tile.split(' ')
        x = int(name[1])
        y = int(name[0])
        adjes = [' '.join([str(y+2), str(x+1)]), ' '.join([str(y+2), str(x-1)]), ' '.join([str(y), str(x+2)]), ' '.join([str(y), str(x-2)]), ' '.join([str(y-2), str(x+1)]), ' '.join([str(y-2), str(x-1)]), ' '.join([str(y), str(x)])]
        for t in adjes:
            if not t == tile:
                if t in dic:
                    if dic[t]['black'] == True:
                        c2 += 1
        if dic[tile]['black'] == True:
            if c2 == 0 or c2 > 2:
                newT['black'] = False
            else:
                newT['black'] = True
        else:
            if c2 == 2:
                newT['black'] = True
            else:
                newT['black'] = False
        newD[tile] = newT
    return newD

i = 1
old = tiles.copy()
while i < 101:
    old = simulateDay(old).copy()
    c3 = 0
    for hh in old:
        if old[hh]['black']:
            c3 += 1
    print(i)
    i += 1
    if i == 101:
        print(c3)
