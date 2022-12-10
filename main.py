from collections import defaultdict
import numpy as np
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


####################################################################################################################
#                                                    Day 6                                                         # 
####################################################################################################################
print("\nDAY 6 Solution")

signal = ""
f6 = open("input6.txt", "r")

for x in f6:
    signal = x[:-1]
f6.close()

def check_marker_occurence(str, s, i):
    b = True
    while(b):
        current_chars = str[s:i]
        has_repeated_chars = len(set(current_chars)) != len(current_chars)
        if has_repeated_chars:
            s += 1
            i += 1
        else:
            b = False
    print("First marker after character: %d" % i)

check_marker_occurence(signal, 0, 4)    #1134
check_marker_occurence(signal, 0, 14)   #2263


####################################################################################################################
#                                                    Day 7                                                         # 
####################################################################################################################
print("\nDAY 7 Solution")

terminal = []
f7 = open("input7.txt", "r")

for x in f7:
    terminal.append(x.split("\n")[0])
f7.close()
terminal.append("$ cd ..")

dir_arr = []
dir_name = []
numbers = ['0','1','2','3','4','5','6','7','8','9']
for command in terminal:
    if "$ cd " in command:
        dir = command.split(' ')[2]
        if dir != "..":
            dir_name.append((dir,0))
        else:
            copied = dir_name.copy()
            dir_arr.append(copied)
            dir_name.pop()
    if command[0] in numbers:
        size = int(command.split(' ')[0])
        dir_name = [(d,s+size) for (d,s) in dir_name]

directories = []
root = dir_arr[-1][0][1]
sum_d = 0
for every_dir in dir_arr:
    directories.append(every_dir[-1][1])
    sum_d += every_dir[-1][1]
directories.append(root)

under100k = [size for size in directories if size <= 100000]
total_size = sum(under100k)

space_to_be_freed = 30000000 - (70000000 - root)
directories.sort()
delete_dir = next(x[0] for x in enumerate(directories) if x[1] >= space_to_be_freed)

print("Sum of total sizes: %d" % total_size)    # 1232307
print("Size of directory to be deleted: %d " % directories[delete_dir]) #7268994


####################################################################################################################
#                                                    Day 8                                                         # 
####################################################################################################################
print("\nDAY 8 Solution")

f8 = open("input8.txt", "r")
arr_list = []
for line in f8:
    rows = line.split('\n')[0]
    elems = [int(x) for x in rows]
    arr_list.append(elems)
f8.close()

arr = np.array(arr_list)
scenic_scores = []

def compute_scenic_score(left, right, up, down):
    score = np.prod([left, right, up, down])
    return score

def find_next_taller_tree(tree_height, area, inorder):
    index_pos = 0
    if inorder:
        pos = next(x[0] for x in enumerate(area) if x[1] >= tree_height)
        index_pos = pos
    else:
        area.reverse()
        pos = next(x[0] for x in enumerate(area) if x[1] >= tree_height)
        index_pos = len(area) - pos -1
    return index_pos

def is_visible(arr, row, col):
    visible = False
    tree_height = arr[row][col]
    left_from_tree = arr[row][:col]
    right_from_tree = arr[row][col+1:]
    above_from_tree = arr[0::, col][0:row]
    down_from_tree = arr[0::, col][row+1:]
    
    max_l = max(left_from_tree)
    max_r = max(right_from_tree)
    max_a = max(above_from_tree)
    max_d = max(down_from_tree)

    look_left, look_right, look_up, look_down = 0, 0, 0, 0
    if tree_height > max_l:
        visible = True
        look_left = len(left_from_tree)
    else:
        index_pos = find_next_taller_tree(tree_height, list(left_from_tree), False)
        look_left = col - index_pos

    if tree_height > max_r:
        visible = True
        look_right = len(right_from_tree)
    else:
        index_pos = find_next_taller_tree(tree_height, list(right_from_tree), True)
        look_right = index_pos+1

    if tree_height > max_a:
        visible = True
        look_up = len(above_from_tree)
    else:
        index_pos = find_next_taller_tree(tree_height, list(above_from_tree), False)
        look_up = row - index_pos

    if tree_height > max_d:
        visible = True
        look_down = len(down_from_tree)
    else:
        index_pos = find_next_taller_tree(tree_height, list(down_from_tree), True)
        look_down = index_pos+1

    scenic_scores.append(compute_scenic_score(look_left, look_right, look_up, look_down))
    return visible

bool_mat = np.ones((len(arr), len(arr[0])), dtype=bool)

for i in range(1, len(arr)-1):
    for j in range(1, len(arr[0])-1):
        bool_mat[i,j] = is_visible(arr, i, j)

print("Visible trees: %d" % bool_mat.sum())     #1733
print("Highest scenic score: %d" % max(scenic_scores))  #284648


####################################################################################################################
#                                                    Day 9                                                         # 
####################################################################################################################
print("\nDAY 9 Solution")

f9 = open("input9.txt", "r")
motions = []
for line in f9:
    rows = line.split('\n')[0]
    r = rows.split(' ')
    elems = (r[0],int(r[1]))
    motions.append(elems)
f9.close()

def is_touching(head, tail): # return True if two knots are touching
    h_i, h_j = head[0], head[1]
    t_i, t_j = tail[0], tail[1]
    if t_j == h_j-1 and t_i in [h_i-1, h_i, h_i +1]:
        return True
    if t_j == h_j and t_i in [h_i-1, h_i, h_i +1]:
        return True
    if t_j == h_j+1 and t_i in [h_i-1, h_i, h_i +1]:
        return True
    return False

def move_tail(head, tail, my_grid, changeGrid): 
    h_i, h_j = head[0], head[1]
    t_i, t_j = tail[0], tail[1]
    new_tail_pos = (t_i,t_j)
    if h_i != t_i and h_j != t_j: # move diagonally
        if abs(h_i-t_i) == 1:
            if h_j > t_j:
                if changeGrid: my_grid[h_i,h_j-1] = True
                new_tail_pos =(h_i,h_j-1)
            else:
                if changeGrid: my_grid[h_i,h_j+1] = True
                new_tail_pos = (h_i,h_j+1)
        elif abs(h_j-t_j) == 1:
            if h_i < t_i:
                if changeGrid: my_grid[h_i+1,h_j] = True
                new_tail_pos = (h_i+1,h_j)
            else:
                if changeGrid: my_grid[h_i-1,h_j] = True
                new_tail_pos = (h_i-1,h_j)
        else: 
            if h_i > t_i:
                if h_j < t_j:
                    if changeGrid: my_grid[h_i-1, t_j-1] = True
                    new_tail_pos = (h_i-1, t_j-1)
                else:
                    if changeGrid: my_grid[h_i-1, t_j+1] = True
                    new_tail_pos = (h_i-1, t_j+1)
            else:
                if h_j < t_j:
                    if changeGrid: my_grid[h_i+1, t_j-1] = True
                    new_tail_pos = (h_i+1, t_j-1)
                else:
                    if changeGrid: my_grid[h_i+1, t_j-1] = True
                    new_tail_pos = (h_i+1, t_j+1)
    elif h_i == t_i: # move along row
        if h_j > t_j:
            if changeGrid: my_grid[h_i, h_j-1] = True
            new_tail_pos = (h_i, h_j-1)
        else:
            if changeGrid: my_grid[h_i, h_j+1] = True
            new_tail_pos = (h_i, h_j+1)
    else:   # move along column
        if h_i > t_i:
            if changeGrid: my_grid[h_i-1, h_j] = True
            new_tail_pos = (h_i-1, h_j)
        else:
            if changeGrid: my_grid[h_i+1, h_j] = True
            new_tail_pos = (h_i+1, h_j)
    return new_tail_pos

def move_all(way, head, tail, knots, grid):
    new_head_pos = [head[0],head[1]]
    new_tail_pos = [tail[0],tail[1]]
    new_knots = [kn for kn in knots]
    if way =='R':       new_head_pos[1] = head[1]+1
    elif way == 'U':    new_head_pos[0] = head[0]-1
    elif way == 'L':    new_head_pos[1] = head[1]-1
    elif way == 'D':    new_head_pos[0] = head[0]+1

    last_visited_node = new_head_pos
    if knots != []:
        if is_touching(new_head_pos, new_knots[0]) == False:
            new_knot = move_tail(new_head_pos, new_knots[0], grid, False)
            new_knots[0] = new_knot
        for i in range(1, len(knots)):
            if is_touching(new_knots[i-1], new_knots[i]) == False:
                new_k = move_tail(new_knots[i-1], new_knots[i], grid, False)
                new_knots[i] = new_k
            i += 1
        last_visited_node = new_knots[-1]
    if is_touching(last_visited_node, new_tail_pos) == False:
        new_tail = move_tail(last_visited_node, new_tail_pos, grid, True)
        new_tail_pos = new_tail
    return new_head_pos, new_tail_pos, new_knots

grid1 = np.zeros((500,500), dtype=bool)
grid2 = np.zeros((500,500), dtype=bool)
s = [len(grid1)//2, len(grid1)//2]

grid1[s[0],s[1]], grid2[s[0],s[1]] = True, True

knots1, knots2 = [], [s,s,s,s,s,s,s,s]
head1, tail1, head2, tail2 = s, s, s, s 

for m in motions:
    for i in range(m[1]):
        head1, tail1, knots1= move_all(m[0],head1,tail1,knots1,grid1)
        head2, tail2, knots2 = move_all(m[0], head2, tail2, knots2, grid2)

print("Number of positions visited by the tail Part1: %d" % grid1.sum()) #5883
print("Number of positions visited by the tail Part2: %d" % grid2.sum()) # 2367


####################################################################################################################
#                                                    Day 10                                                        # 
####################################################################################################################
print("\nDAY 10 Solution")

f10 = open("input10.txt", "r")
program = []
cycle = 1
for line in f10:
    l = line.split('\n')[0]
    i = [cycle, l]
    if l =='noop': cycle += 1
    else: cycle += 2
    program.append(i)
f10.close()

def calculate_x(x, cycle, program):
    findIndex = [i for i, p in list(enumerate(program)) if p[0] == cycle or p[0]+1 == cycle]
    for i in range(0, findIndex[0]):
        if "addx" in program[i][1]:
            x += int(program[i][1].split(' ')[1])
    return x

# for Part2 calculates the new value of x after 1 cycle
def calculate_x2(x, cycle, program):
    findIndex = [i for i, p in list(enumerate(program)) if p[0] == cycle or p[0]+1 == cycle]
    for i in range(0, findIndex[0]):
            if "addx" in program[i][1]:
                x += int(program[i][1].split(' ')[1])
    if program[findIndex[0]][0] != cycle:
        if "addx" in program[findIndex[0]][1]:
                x += int(program[findIndex[0]][1].split(' ')[1])
    return x

signals = 0
cycles = [20,60,100,140,180,220]
for c in cycles:
    signals += c * calculate_x(1,c,program)

print("Sum of signals: %d" % signals) # 12880

current_crt_row = []
pixels = [1,2,3] # positions of ### in the sprite
cycles2 = [40,80,120,160,200,240]
i = 1
for cycle in range(1, 241):
    if i in pixels: current_crt_row.append('#')
    else: current_crt_row.append('.')
    x = calculate_x2(1,cycle,program)
    pixels = [x,x+1,x+2]
    i += 1
    if cycle in cycles2:
        word = " ".join(current_crt_row)
        print(word)
        current_crt_row.clear()
        i = 1

