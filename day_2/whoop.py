twice = 0
threes = 0

# get file split into lines
with open('input.txt') as r:
    lines = r.readlines()

# for each line
for line in lines:
    check_two = False
    check_three = False
    # check each char in line
    for char in set(line):
        if line.count(char) == 2 and not check_two:
            check_two = True
            twice +=1
        if line.count(char) == 3 and not check_three:
            check_three = True
            threes +=1


checksum = twice * threes # checksum thing
print("part 1: " + str(checksum)) #6370


for line in lines: # first line loop- line 1
    for linee in lines: # second line loop- line 2
        change = 0 # store number of changes to line
        change_pos = 0 # store position of change in the line
        if line == linee: # if line 1 to line 2 is the same
            continue # not correct so pass
        for i in range(len(line)): # for length of line
            if line[i] != linee[i]: # compare line 1 to line 2
                change +=1 # add one to change
                change_pos = i # store position of line change
        if change == 1: # if there's only one change
            # concatenate line before changed letter & after changed letter
            answer = line[:change_pos] + line[change_pos+1:]


print("part 2: " + answer) # rmyxgdlihczskunpfijqcebtv
