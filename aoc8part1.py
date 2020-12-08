from codereader import imboi

f = open('./h.csv').read().split('\n')

e = []

for a in f:
    e.append(a.split(' '))

gb = imboi([], e, 0, False, False, 0)
while True:
    gb.execute()
    if gb.looped:
        break
print(gb.acc)