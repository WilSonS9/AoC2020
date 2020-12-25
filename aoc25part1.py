card = 3469259
door = 13170438
cardLoop = 0
def transform(initial, subject):
    return (subject*initial) % 20201227
i = 0
init = 1
while True:
    init = transform(init, 7)
    i += 1
    if init == card:
        cardLoop = i
        break
j = 0
ab = 1
while j < cardLoop:
    ab = transform(ab, door)
    j += 1
print(ab)