f = open('./m.csv').read().split('\n')

# The key to solving this is the Chinese Remainder Theorem, which the code below executes
# You can also do this online at https://comnuan.com/cmnn02/cmnn0200a/cmnn0200a.php to solve your linear system of congruences

e = f[1].replace('x,', '').replace(',,', ',').split(',')
e2 = f[1].split(',')

def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if (x1 < 0):
        x1 = x1 + m0

    return x1

def findMinX(num, rem, k): 
    prod = 1
    for i in range(0, k):
        prod = prod * num[i]
    result = 0
    for i in range(0,k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp

    return result % prod

num = []
rem = []

for a in e:
    num.append(int(a))
    rem.append(-1*int(e2.index(a)) % int(a))
k = len(num)

print( "x is", findMinX(num, rem, k))