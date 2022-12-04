
####################################################################################################################
#                                                    Day 1                                                         # 
####################################################################################################################
print("DAY 1 Solution")

cals_per_elf, cals = [], []
f = open("input1.txt", "r")

for x in f:
    if x != '\n':
        cals.append(int(x))
    else:
        cals_per_elf.append(sum(cals))
        cals.clear()
f.close()

sortedCals = sorted(cals_per_elf, reverse=True)

print("max cals intake: %d" %sortedCals[0]) #67027
print("Top 3 cals intake in total: %d" %sum(sortedCals[:3])) #197291


####################################################################################################################
#                                                    Day 2                                                         # 
####################################################################################################################
print("\nDAY 2 Solution")

inputList = []
f2= open("input2.txt", "r")
for x in f2:
    y = x.split()
    inputList.append((y[0], y[1]))
f2.close()

#   Rock        A   X   (1)  LOSE
#   Paper       B   Y   (2)  DRAW
#   Scissors    C   Z   (3)  WIN        
def calculateScore(op, choice, strategy):
    strat1 = [ ('A','X',3), ('A','Y',6), ('A','Z',0),
                ('B','X',0), ('B','Y',3), ('B','Z',6),
                ('C','X',6), ('C','Y',0), ('C','Z',3)]
    strat2 = [ ('A','X',3), ('A','Y',1), ('A','Z',2),
                ('B','X',1), ('B','Y',2), ('B','Z',3),
                ('C','X',2), ('C','Y',3), ('C','Z',1)]
    shapes = [('X',1), ('Y',2), ('Z',3)]
    outcome = [('X',0), ('Y',3), ('Z',6)]

    firstScore, secondScore = 0, 0
    if(strategy == 1):
        for (a,x,v) in strat1:
            if op == a and choice == x:
                secondScore = v
                firstScore = [val for c, val in shapes if c == x][0]
    else:
        for (a,x,v) in strat2:
            if op == a and choice == x:
                firstScore = v
                secondScore = [val for o, val in outcome if o == x][0]
    
    return firstScore+secondScore

totalScores1, totalScores2 = 0, 0
for (x,y) in inputList:
    totalScores1 += calculateScore(x,y,1)
    totalScores2 += calculateScore(x,y,2)
    
print("Total Scores (first strategy): %d" %totalScores1) #12458
print("Total Scores (second strategy): %d" %totalScores2) #12683


####################################################################################################################
#                                                    Day 3                                                         # 
####################################################################################################################
print("\nDAY 3 Solution")

rucksackList, badgeList = [], []
f3= open("input3.txt", "r")
for x in f3:
    badgeList.append(x[:-1]) # for Part2
    y1 = x[:len(x)//2]
    y2 = x[len(x)//2:]
    rucksackList.append((y1, y2))
f3.close()

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
enumChar = list(enumerate(chars, start=1))

char_values = []
for(y1,y2) in rucksackList:
    common_chars = ''.join([c for c in y1 if c in y2])
    char_values.append([v for v, c in enumChar if c == common_chars[0]][0])
print("Result Part 1: %d" %(sum(char_values))) #8515

# PART 2
subList = [badgeList[n:n+3] for n in range(0, len(badgeList), 3)]

char_values.clear()
for s in subList:
    common_chars = ''.join([c for c in s[0] if c in s[1]])
    common_chars_all = ''.join([c for c in common_chars if c in s[2]])
    char_values.append([v for v, c in enumChar if c == common_chars_all[0]][0])
print("Result Part 2: %d" %(sum(char_values))) #2434


