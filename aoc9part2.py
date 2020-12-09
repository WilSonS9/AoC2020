f = open('./i.csv').read().split('\n')
from time import time
t1 = time()
def func():
    for width in range(1,len(f)):
        for h in range(0,len(f)-width-1):
            li = []
            for j in range(0,width+1):
                li.append(int(f[h+j]))
            if sum(li) == 556543474: #Output from part 1
                return sorted(li)[0] + sorted(li)[len(li)-1]
print(func(), time()-t1)