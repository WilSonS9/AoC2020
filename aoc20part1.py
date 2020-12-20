import numpy as np

f = open('./u.csv').read().replace('Tile ', '').split('\n\n')

large = {}

for a in f:
    a = a.split(':\n')
    name = a[0]
    rest = a[1].split('\n')
    li = []
    for b in rest:
        li.append([list(b)][0])
    m = np.matrix(li)
    newDict = {'name': name, 'tile': m}
    large[name] = newDict

def getCols(mat):
    return(mat[:,0], mat[:,9])

def getRows(mat):
    return(mat[0,:], mat[9,:])

matricesLarge = []
ul = []
dl = []
ur = []
dr = []

for key,val in large.items():
    matr2 = val['tile']
    matrices3 = [matr2, np.rot90(matr2, 1), np.rot90(matr2, 2), np.rot90(matr2, 3)]
    matrices4 = []
    for y in matrices3:
        matrices4.append(y)
        matrices4.append(np.flipud(y))
    matricesLarge.append(matrices4)

corners = []
for key,dic in large.items():
    mat = dic['tile']
    matrices = [mat, np.rot90(mat, 1), np.rot90(mat, 2), np.rot90(mat, 3)]
    for xy in matrices:
        upper = 0
        lower = 0
        left = 0
        right = 0
        for yzz in matricesLarge:
            for yz in yzz:
                cols1 = getCols(xy)
                cols2 = getCols(yz)
                rows1 = getRows(xy)
                rows2 = getRows(yz)
                if np.array_equal(cols1[1], cols2[0]):
                    right += 1
                elif np.array_equal(cols1[0], cols2[1]):
                    left += 1
                elif np.array_equal(rows1[1], rows2[0]):
                    lower += 1
                elif np.array_equal(rows1[0], rows2[1]):
                    upper += 1
        if upper == 0 or lower == 0:
            if left == 0 or right == 0:
                corners.append(int(dic['name']))
c2 = 1
for x in set(corners):
    c2 *= x
print(c2)