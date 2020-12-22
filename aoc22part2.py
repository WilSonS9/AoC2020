from collections import deque
from itertools import islice

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

def do(p1, p2):
    n1 = int(p1[0])
    n2 = int(p2[0])
    coolBool1 = n1<=len(p1)-1
    coolBool2 = n2<=len(p2)-1
    top1 = str(n1)
    top2 = str(n2)
    if coolBool1 and coolBool2:
        p1.popleft()
        p2.popleft()
        newp1 = deque(islice(p1, 0, n1))
        newp2 = deque(islice(p2, 0, n2))
        res = game(newp1, newp2, [])
        p1.appendleft(top1)
        p2.appendleft(top2)
        if res[1]:
            winner = p1
            loser = p2
        else:
            winner = p2
            loser = p1
        winner.append(winner[0])
        winner.append(loser[0])
        loser.popleft()
        winner.popleft()
    else:
        if n1 > n2:
            winner = p1
            loser = p2
        else:
            winner = p2
            loser = p1
        winner.append(winner[0])
        winner.append(loser[0])
        loser.popleft()
        winner.popleft()
    return (p1, p2)

count = 0
pp1 = player1.copy()
pp2 = player2.copy()

def game(pp1, pp2, played):
    play1 = pp1.copy()
    play2 = pp2.copy()
    while True:
        p1Deck = play1.copy()
        p2Deck = play2.copy()
        li = [p1Deck, p2Deck]
        if li in played:
            return (pp1, True)
        played.append(li)
        result = do(play1, play2)
        play1 = result[0].copy()
        play2 = result[1].copy()
        if len(play1) == 0 or len(play2) == 0:
            if len(play1) == 0:
                win = play2
                return (win, False)
            elif len(play2) == 0:
                win = play1
                return (win, True)

def counting():
    c = 0
    resulter = game(player1, player2, [])
    winner = resulter[0]
    i = len(winner)
    while i > 0:
        c += (len(winner)-i+1)*int(winner[i-1])
        i -= 1
    print(c)

counting()