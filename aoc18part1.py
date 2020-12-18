f = open('./s.csv').read().replace('(', '( ').replace(')', ' )').split('\n')

d = []
for a in f:
    d.append(a.split(' '))

def isInt(num):
    try:
        num = int(num)
        return True
    except:
        return False


def find_parentheses(s):
    stack = []
    parentheses_locs = {}
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            try:
                parentheses_locs[stack.pop()] = i
            except IndexError:
                raise IndexError('Too many close parentheses at index {}'
                                                                .format(i))
    if stack:
        raise IndexError('No matching close parenthesis to open parenthesis '
                         'at index {}'.format(stack.pop()))
    return parentheses_locs


def evalNoParans(g):
    if type(g) == str:
        g = list(g)
    i = 0
    while i < len(g):
        if isInt(g[i]):
            try:
                if isInt(g[i+2]):
                    string = str(g[i]) + str(g[i+1]) + str(g[i+2])
                    replace = str(eval(string))
                    del g[i+2]
                    del g[i+1]
                    g[i] = replace
                elif g[i+2] == '(':
                    fa = evalParans(g)
                    return fa
            except:
                return g[0]
        elif g[i] == '(':
            far = evalParans(g)
            return far

def evalParans(li):
    parans = find_parentheses(li)
    opens = []
    closes = []
    paranVals = []
    li2 = []
    i = 0
    while i < len(li):
        if li[i] == '(':
            opens.append(i)
        elif li[i] == ')':
            closes.append(i)
        i += 1
    opens2 = opens
    j = 0
    while j < len(opens):
        numInside = 0
        for key,val in parans.items():
            if key > opens[j] and val < parans[opens[j]]:
                numInside += 1
        if not j == len(opens)-1:
            if opens[j+1] > closes[j]:
                new = li[opens[j]+1:closes[j]]
                val = str(evalNoParans(new))
                paranVals.append(val)
            else:
                new = li[opens[j]+1:parans[opens[j]]]
                for ee in reversed(range(1,numInside+1)):
                    x1 = opens[j+ee]
                    x2 = parans[opens[j+ee]]
                    closes.remove(x2)
                    opens.remove(x1)
                val = str(evalParans(new))
                paranVals.append(val)
        else:
            new = li[opens[j]+1:closes[j]]
            val = str(evalNoParans(new))
            paranVals.append(val)
        j += 1
    k2 = 0
    k = 0
    while k < len(li):
        if not li[k] == '(':
            if not li[k] == ')':
                li2.append(li[k])
                k += 1
            else:
                li2.append(paranVals[k2])
                k += parans[opens2[k2]]+1
                k2 += 1
        else:
            li2.append(paranVals[k2])
            k = parans[opens2[k2]]+1
            k2 += 1
    return evalNoParans(li2)

evalNoParans(d[0])
carr = []

for ghj in d:
    carr.append(int(evalNoParans(ghj)))

print(sum(carr))