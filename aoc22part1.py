from collections import deque

f = open('./w.csv').read().replace('Player 1:\n', '').replace('Player 2:\n', '').split('\n\n')

e = []
d = []

for a in f:
    e.append(a.split('\n'))

for b in e:
    li = []
    for h in b:
        li.append(int(h))
    d.append(li)

player1 = deque(e[0])
player2 = deque(e[1])

def do():
    n1 = int(player1[0])
    n2 = int(player2[0])
    if n1 > n2:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1
    winner.append(winner[0])
    winner.append(loser[0])
    loser.popleft()
    winner.popleft()

count = 0

while True:
    if len(player1) == 0 or len(player2) == 0:
        if len(player1) == 0:
            win = player2
        elif len(player2) == 0:
            win = player1
        print(win)
        i = len(win)
        while i > 0:
            count += (len(win)-i+1)*int(win[i-1])
            i -= 1
        break
    else:
        do()

print(count)