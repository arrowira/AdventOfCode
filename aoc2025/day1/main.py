num = 50
res = 0

with open('aoc2025/day1/input.txt', 'r') as f:
    for line in f:
        print(f"{line=}")
        firstCorrection = True
        prevNum = num
        if line[0] == "R":
            num += int(line[1:])
            while num > 99:
                num-=100
                if True or prevNum!=0:
                    res+=1
                    print("right overflow score")
        if line[0] == "L":
            num -= int(line[1:])
            if prevNum == 0 and num<0:
                num+=100
           
            while num < 0:
                num+=100
                if True or prevNum!=0:
                    res+=1
                    print("left overflow score")
        if num == 0 and line[0] == "L":
            res+=1
            print("finishedOnZero")
        
print(res)
