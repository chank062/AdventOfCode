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
