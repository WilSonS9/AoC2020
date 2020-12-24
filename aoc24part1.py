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
    if s in tiles:
        tiles[s] = not tiles[s]
    else:
        tiles[s] = True

count = 0
for key in tiles:
    if tiles[key] == True:
        count += 1

print(count)