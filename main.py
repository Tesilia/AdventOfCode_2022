
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

print("Max cals intake: %d" %sortedCals[0]) #67027
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


####################################################################################################################
#                                                    Day 4                                                         # 
####################################################################################################################
print("\nDAY 4 Solution")

cleaningList = []
f4= open("input4.txt", "r")
for x in f4:
    y = x.split(',')
    z = y[0].split('-')
    z2 = y[1][:-1].split('-')
    cleaningList.append((int(z[0]), int(z[1]), int(z2[0]), int(z2[1])))
f4.close()

def includesSection(a, b, x, y):
    # check if a-b is included in x-y
    if(a >= x and b <= y):
        #print(a,b,x,y)
        return True
    #check if x-y is included in a-b
    if (x >= a and y <= b):
        #print(a,b,x,y)
        return True
    else:
        return False

def overlaps(a, b, x, y):
    if(x <= a and a <= y):
        return True
    if(a <= x and b >= y):
        return True
    if (x <= b and b <= y):
        return True
    else:
        return False

count_included_sections = 0
for (a,b,x,y) in cleaningList:
    if(includesSection(a,b,x,y)):
        count_included_sections += 1

count_contained_at_all = 0
for (a,b,x,y) in cleaningList:
    if(overlaps(a,b,x,y)):
        count_contained_at_all += 1


print("Number of fully contained sections: %d" % count_included_sections)
print("Number of contained sections: %d" % count_contained_at_all)


####################################################################################################################
#                                                    Day 5                                                         # 
####################################################################################################################
print("\nDAY 5 Solution") # result: CMZ

#    [C]         [Q]         [V]    
#    [D]         [D] [S]     [M] [Z]
#    [G]     [P] [W] [M]     [C] [G]
#    [F]     [Z] [C] [D] [P] [S] [W]
#[P] [L]     [C] [V] [W] [W] [H] [L]
#[G] [B] [V] [R] [L] [N] [G] [P] [F]
#[R] [T] [S] [S] [S] [T] [D] [L] [P]
#[N] [J] [M] [L] [P] [C] [H] [Z] [R]

crates = [[''], ['N', 'R', 'G', 'P'], 
                ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'], 
                ['M', 'S', 'V'], 
                ['L', 'S', 'R', 'C', 'Z', 'P'],
                ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
                ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
                ['H', 'D', 'G', 'W', 'P'],
                ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
                ['R', 'P', 'F', 'L', 'W', 'G', 'Z']]
steps = []

f5= open("input5.txt", "r")
for x in f5:
    y = x.split(' ')
    steps.append((int(y[1]), int(y[3]), int(y[5][0])))
f5.close()

def moveCrates(m, f, t):
    crates_to_move = crates[f][-m:]
    #crates_to_move.reverse()           #undo comment for Part1
    crates[t].extend(crates_to_move)

    i = 1
    while i <= m:
        crates[f].pop()
        i += 1

for (m,f,t) in steps:
    moveCrates(m,f,t)

msg = ""
for i in list(range(len(crates)-1)):
    msg += crates[i+1].pop()
print("Crates on top of each stack: " + msg)

