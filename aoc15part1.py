f = open('./o.csv').read().split(',')
e = []
for a in f:
    e.append(a)
while len(e) < 2020:
    i = 0
    most = 0
    char = e[len(e)-1]
    i = 0
    while i < len(e):
        if e[i] == char and not i == len(e)-1:
            most = i+1
        i += 1
    pusher = len(e) - most
    if most == 0:
        e.append('0')
    else:
        e.append(str(pusher))
print(e[len(e)-1])