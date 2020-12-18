from functools import reduce
from operator import mul
f = open('s.csv')
c1 = 0
for l in f:
    l = '(' + l.strip() + ')'
    l = l.replace('*', ',')
    l = l.replace('(', 'reduce(mul, (')
    l = l.replace(')', ',))')
    c1 += eval(l)
print(c1)