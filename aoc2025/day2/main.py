numbers ="1234567890"

res = 0
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
def isDouble(num):
    strNum = str(num)
    return strNum[:int(len(strNum)/2)] == strNum[int(len(strNum)/2):]
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
                
                for i in range(minNumber, maxNumber+1):
                    if isDouble(i):
                        res+=i
                        print(i)


                newRange()
print(res)