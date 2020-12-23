from collections import defaultdict, deque

def do():
    e = deque([8,7,2,4,9,5,1,3,6] + list(range(10, 1000001)))
    comesAfter = defaultdict(list)

    def getNext():
        nextElt = e.popleft()
        if nextElt in comesAfter:
            e.extendleft(comesAfter[nextElt][::-1])
            del comesAfter[nextElt]
        return nextElt
    c2 = 1
    while c2 < 10000001:
        curCup = getNext()
        pickCups = [getNext(), getNext(), getNext()]
        unavailableCups = set([curCup] + pickCups)

        destination = curCup
        while destination in unavailableCups:
            destination -= 1
            if destination < 1:
                destination = 1000000
        comesAfter[destination] += pickCups
        e.append(curCup)
        c2 += 1

    while (nextt := getNext()) != 1:
        e.append(nextt)

    n1, n2 = getNext(), getNext()
    return n1 * n2

print(do())