import math

f = open('./e.csv').read().split('\n')

ids = []

for seat in f:
    high = 127
    low = 0
    high2 = 7
    low2 = 0
    for ch in seat:
        if ch == 'F':
            high = math.floor((high+low)/2)
        elif ch == 'B':
            low = math.ceil((high+low)/2)
        elif ch == 'L':
            high2 = math.floor((high2+low2)/2)
        elif ch == 'R':
            low2 = math.ceil((high2+low2)/2)
    ids.append(8*high + high2)

ids.sort(key=lambda x: x)

i = 0

while i < len(ids)-1:
    if ids[i+1] - ids[i] == 2:
        print(ids[i]+1)
        break
    i += 1