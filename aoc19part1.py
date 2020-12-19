f = open('./t2.csv').read().replace('"', '').split('\n\n')
rules = f[0].split('\n')
messages = f[1].split('\n')
large = {}

for a in rules:
    s = a.split(': ')
    name = s[0]
    largeList = []
    possibles = s[1].split(' | ')
    for b in possibles:
        largeList.append(b.split(' '))
    newDict = {'name': name, 'rules': largeList}
    large[name] = newDict

match = large['0']
stringList = []
test = 'abbbab'

def follows(string, rule, i):
    j = i
    for c in rule['rules']:
        j = i
        count = 0
        if c[0].isalpha():
            if j < len(string):
                if string[j] == str(rule['rules'][0][0]):
                    j += 1
                    count += 1
            else:
                break
        else:
            for d in c:
                ab = follows(string, large[d], j)
                if ab[0]:
                    count += 1
                    j = ab[1]
                else:
                    break
        if count == len(rule['rules'][0]):
            return (True, j)
    return (False, j)

c2 = 0
for xy in messages:
    abc = follows(xy, match, 0)
    if abc[0] and abc[1] >= len(xy):
        c2 += 1

print(c2)