class imboi:
    def __init__(self, iList, inp, acc, fin, looped, i):
        self.iList = iList
        self.inp = inp
        self.acc = acc
        self.fin = fin
        self.looped = looped
        self.i = i
    def execute(self):
        if self.inp[self.i][0] == 'acc':
            self.acc += int(self.inp[self.i][1])
            self.i += 1
        elif self.inp[self.i][0] == 'jmp':
            self.i += int(self.inp[self.i][1])
        elif self.inp[self.i][0] == 'nop':
            self.i += 1
        if self.i in self.iList:
            self.looped = True
        self.iList.append(self.i)
        if self.i >= len(self.inp):
            self.fin = True