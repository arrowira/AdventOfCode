map = []
sum = 0
def printMap(array):
        for i in array:
            print(i)
def wholeThing(map):
    global sum

    
    def checkSpot(x, y):
        if map[r+y][c+x] == "@":
            return True
        return False

    res = 0
    

        
    for r in range(len(map)):
        for c in range(len(map[0])):
            adjacentPapers = 0
            #is paper?
            if map[r][c]=="@":

                #check adjacent 8 positions
                
                #check top room
                if r>0:
                    #check top spots
                    if checkSpot(0,-1):
                        adjacentPapers+=1
                    if c>0:
                        if checkSpot(-1,-1):
                            adjacentPapers+=1
                    if c<len(map[0])-1:
                        if checkSpot(1,-1):
                            adjacentPapers+=1
                #check bottom room
                if r<len(map)-1:
                    #check botoom spots
                    if checkSpot(0,1):
                        adjacentPapers+=1
                    if c>0:
                        if checkSpot(-1,1):
                            adjacentPapers+=1
                    if c<len(map[0])-1:
                        if checkSpot(1,1):
                            adjacentPapers+=1
                #check left room
                if c>0:
                    if checkSpot(-1,0):
                        adjacentPapers+=1
                #check right room
                if c<len(map[0])-1:
                    if checkSpot(1,0):
                        adjacentPapers+=1
                if adjacentPapers < 4:
                    map[r][c]="."
                    
                    res+=1
    print("res: "+str(res))
    sum+=res
    return (map,res)

with open('aoc2025/day4/input.txt', 'r') as f:
        #copy file
        for line in f:
            newRow = []
            for c in line:
                if c != "\n":
                    newRow.append(c)
            map.append(newRow)
while wholeThing(map)[1]!=0:
    pass

print(sum)