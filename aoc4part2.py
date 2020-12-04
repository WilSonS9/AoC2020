f = open('./d.csv').read().replace(' ', '\n').split('\n\n')
e = []
g = []
count = 0
for a in f:
    e += [a.replace('\\n', '\n').split('\n')]
for gn in e:
    bg = 0
    valid = 0
    if len(gn) >= 7:
        for hgd in gn:
            temp = hgd.split(':')
            if temp[0] == 'byr':
                if 1920<=int(temp[1])<=2002:
                    valid += 1
            elif temp[0] == 'iyr':
                if 2010<=int(temp[1])<=2020:
                    valid += 1
            elif temp[0] == 'eyr':
                if 2020<=int(temp[1])<=2030:
                    valid += 1
            elif temp[0] == 'hgt':
                if temp[1][len(temp[1])-2:len(temp[1])] == 'cm' and 150<=int(temp[1][0:len(temp[1])-2])<=193:
                    valid += 1
                elif temp[1][len(temp[1])-2:len(temp[1])] == 'in' and 59<=int(temp[1][0:len(temp[1])-2])<=76:
                    valid += 1
            elif temp[0] == 'hcl':
                ghueoa = 0
                if temp[1][0:1] == '#':
                    for ch in temp[1][1:len(temp[1])]:
                        if ch in 'abcdef0123456789':
                            ghueoa += 1
                    if ghueoa == 6:
                        valid += 1
            elif temp[0]=='ecl':
                if temp[1] in 'amb blu brn gry grn hzl oth':
                    valid += 1
            elif temp[0]=='pid':
                try:
                    rjgos=int(temp[1])
                    if len(temp[1]) == 9:
                        valid += 1
                except:
                    pass
        if valid == 7:
            count += 1
print(count)