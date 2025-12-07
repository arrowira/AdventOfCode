numbers ="1234567890"


minNumber = 0
maxNumber = 0
minNumberStr = ""
maxNumberStr = ""
postDash = False
def newRange():
    global minNumber,maxNumber,minNumberStr,maxNumberStr,postDash
    minNumber = 0
    maxNumber = 0
    minNumberStr = ""
    maxNumberStr = ""
    postDash = False
def isInvalid(num):
    strNum = str(num)
    repLen = 1

    while repLen<len(strNum):
        if len(strNum)%repLen == 0:

            char = 0
            broken = False
            lastWindow = ""
            while char < len(strNum)-repLen+1:
                
                if (lastWindow != strNum[char:char+repLen] and char!=0) or (len(strNum[char:char+repLen]) > len(strNum)/2):
                    broken=True
                    
                    break


                lastWindow = strNum[char:char+repLen]
                char+=repLen
                
            if not broken:
                return True
                
        repLen+=1
    return False

 
#string parser
res = 0
with open('aoc2025/day2/input.txt', 'r') as f:
    for line in f:
        print(line)

        

        for col,character in enumerate(line):
            if character in numbers:
                if postDash:
                    maxNumberStr+=character
                else:
                    minNumberStr+=character
            if character == "-":
                postDash = True
            
            if character == "," or col == len(line)-1:
                #end of range
                minNumber = int(minNumberStr)
                maxNumber = int(maxNumberStr)
                print(f"{minNumber=}")
                print(f"{maxNumber=}")
                for i in range(minNumber, maxNumber+1):
                    if isInvalid(i):
                        res+=i
                        print(i)

   
                newRange()
print("res:" + str(res))