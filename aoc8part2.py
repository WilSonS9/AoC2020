from codereader import imboi

f = open('./h.csv').read().split('\n')

e = []
changeCount = 0

for a in f:
    e.append(a.split(' '))

gb1 = imboi([], e, 0, False, False, 0)
while not gb1.fin:
    if gb1.inp[gb1.i][0] == 'jmp':
        e[gb1.i][0] = 'nop'
        gb2 = imboi([], e, 0, False, False, 0)
        while True:
            gb2.execute()
            if gb2.looped:
                e[gb1.i][0] = 'jmp'
                break
            if gb2.fin and changeCount <= 0 and not gb2.looped:
                print(gb2.acc)
                gb1.fin = True
                break
    elif gb1.inp[gb1.i][0] == 'nop':
        e[gb1.i][0] = 'jmp'
        gb2 = imboi([], e, 0, False, False, 0)
        while True:
            gb2.execute()
            if gb2.looped:
                e[gb1.i][0] = 'nop'
                break
            if gb2.fin and changeCount and not gb2.looped <= 0:
                print(gb2.acc)
                gb1.fin = True
                break
    gb1.execute()