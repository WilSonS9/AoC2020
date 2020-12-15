f = open('./o.csv').read().split(',')
e = {}
j = 0
while j < len(f):
    e[int(f[j])] = {'num': int(f[j]), 'occs': [j]}
    j += 1
char = 18 # The latest number
i = 7 # The new index counting from 0
while i < 30000000:
    occs = e[char]['occs']
    if occs[-1] ==  i-1 and len(occs) == 1:
        try:
            e[0]['occs'].append(i)
        except:
            e[0] = {'num': 0, 'occs': [i]}
        char = 0
    else:
        try:
            new = occs[-1] - occs[-2]
        except:
            new = occs[-1]
        try:
            e[new]['occs'].append(i)
        except:
            e[new] = {'num': new, 'occs': [i]}
        char = new
    i += 1
print(e[char]['num'])