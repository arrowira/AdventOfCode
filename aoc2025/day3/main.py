res = 0


with open('aoc2025/day3/input.txt', 'r') as f:
    for line in f:
        contenderD1 = 0
        contenderNum = 0
        
        
        for c,d1 in enumerate(line[:len(line)-2]):
            if d1 !="\n":
                if int(d1)>contenderD1:
                    contenderD1=int(d1)
                    contenderD2 = None
                    for d2 in line[c+1:]:
                        if d2 !="\n":
                            if contenderD2 is None or int(d2)>contenderD2:
                                contenderD2 = int(d2)
                    contenderNum = int(str(contenderD1)+str(contenderD2))
        print(contenderNum)
        res+=contenderNum
print(res)